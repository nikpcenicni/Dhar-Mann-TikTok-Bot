import os
from re import T
import ffmpeg
import pathlib
from moviepy.editor import VideoFileClip
import time
from utilities import downloader, slicer, makevideo, utilties


def removeOutro(filename, end, type):
    
    return cut_at_time(filename, 0, end, type)

def cut_at_time(filename, start ,end, type):
    
    
    #determines the path of the downloaded file to be processed  
    path = os.path.join(os.getcwd(), 'preprocessed')
    if (type == "story" or type == "split"):
        path = os.path.join(path, 'story')
    elif (type == "background" or type == "split-bg"):
        path = os.path.join(path, 'background')
        
    # add the file name to the paths
    filepath = os.path.join(path, filename)
    
    # determines the path to output the clipped video
    output = os.path.join(os.getcwd(), 'processed')
    if (type == "story" or type == "split"):
        output = os.path.join(output, 'story')
    elif (type == "background" or type == "split-bg"):
        output = os.path.join(output, 'background')
    
    if (type == "story"):
        end = int(end[0:2])*60 + int(end[3:6])
        output = os.path.join(output, (filename[:-4]+"_"+str(start)+"_"+str(end)+".mp4"))
    else:
        end = end
    

    #output = os.path.join(output, filename)
    
    
    if type == "split":
        output = os.path.join(output, ("part " + str(utilties.countFiles(output)) +".mp4"))
        
    if type == "split-bg":
        offset = countFiles(output)
        output = os.path.join(output, "background " + str(offset) + ".mp4")
    
    

        
    probe_result=ffmpeg.probe(filepath)
    duration = probe_result.get("format",{}).get("duration",None)
    print(duration)
    
    input_stream = ffmpeg.input(filepath)
    
    pts = "PTS-STARTPTS"
    if (type == "split-bg"):
        video = input_stream.trim(start = start, end = end).setpts(pts).filter('crop', '1/3*in_w', '2/3*in_h')
    else:
         video = input_stream.trim(start = start, end = end).setpts(pts)
    audio = (input_stream
             .filter("atrim", start = start, end = end)
             .filter("asetpts", pts))
    
    video_and_audio = ffmpeg.concat(video, audio, v=1, a=1)
    
    if os.path.exists(output):
        os.remove(output)
    
    video = ffmpeg.output(video_and_audio, output, format="mp4")
    video.run()
    if type != "split" and type != "split-bg":
        os.remove(filepath)
       
        
    return output
    
    

def splitVideoToChunks(input, type):
    path = input
    if (type == "story"):
        path = os.path.join(os.path.join(os.getcwd(), 'preprocessed'), 'story')
        path = os.path.join(path, input)
    elif (type == "background"):
        path = os.path.join(os.getcwd(), 'preprocessed')
        path = os.path.join(path, 'background')
        path = os.path.join(path, input)

    clip = VideoFileClip(path)
    lastChunkTime = clip.duration%180
    numChunks = int(clip.duration/180)
    if (lastChunkTime > 0):
        numChunks += 1
    if (type == "background"):
        numChunks -= 1
    print(numChunks)
    time.sleep(10)
    
    for i in range(numChunks):
        start = i*180
        end = (i+1)*180
        if (i == numChunks-1 and type == "story"):
            end = clip.duration
        print(start, end)
        if type == "background":
            cut_at_time(input, start, end, "split-bg")
        else:
            cut_at_time(input, start, end, "split")
    
    os.remove(input)
    return
    
def countFiles(dir):
    initial_count = 0
    for path in pathlib.Path(dir).iterdir():
        if path.is_file():
            initial_count += 1

    print(initial_count)
    return initial_count