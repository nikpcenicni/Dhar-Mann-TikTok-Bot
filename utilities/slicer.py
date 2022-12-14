import os
from re import T
import ffmpeg
import pathlib
from moviepy.editor import VideoFileClip
import time

from numpy import rint
from utilities import downloader, slicer, makevideo, utilties
from gui import gui


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
        video = input_stream.trim(start = start, end = end).setpts(pts).filter('crop', w='1/3*in_w', h='5/7*in_h')
    else:
         video = input_stream.trim(start = start, end = end).setpts(pts)
    audio = (input_stream
             .filter("atrim", start = start, end = end)
             .filter("asetpts", pts))
    
    if (type == "story" or type == "split"):
        video_and_audio = ffmpeg.concat(video, audio, v=1, a=1)
    else: 
        video_and_audio = ffmpeg.concat(video, v=1).setpts(pts)
    
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
    
    gui.updateProgressBar(0, "Starting Splitting")
    
    offset = ((1/numChunks)/2)*100
    
    for i in range(numChunks):
        start = i*180
        end = (i+1)*180
        if (i == numChunks-1 and type == "story"):
            end = clip.duration
        print(start, end)
        
        if type == "background":
            percent = utilties.calculateProgress(numChunks, i)*100+offset
            gui.updateProgressBar(percent, "Splitting Background")
            cut_at_time(input, start, end, "split-bg")
            percent = utilties.calculateProgress(numChunks, i+1)*100
            gui.updateProgressBar(percent, "Splitting Background")
            
        else:
            percent = utilties.calculateProgress(numChunks, i)*100+offset
            gui.updateProgressBar(percent, "Splitting Story")
            cut_at_time(input, start, end, "split")
            percent = utilties.calculateProgress(numChunks, i+1)*100
            gui.updateProgressBar(percent, "Splitting Background")
            
    
    os.remove(input)
    gui.updateProgressBar(100, "Splitting Complete")
    return
    
def countFiles(dir):
    initial_count = 0
    for path in pathlib.Path(dir).iterdir():
        if path.is_file():
            initial_count += 1

    print(initial_count)
    return initial_count