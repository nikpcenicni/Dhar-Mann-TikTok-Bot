import os
import ffmpeg


def cut_at_time(filename, end, type):
    
    # determines the path to output the clipped video
    output = os.path.join(os.getcwd(), 'processed')
    if (type == 1):
        output = os.path.join(output, 'story')
    elif (type == 2):
        output = os.path.join(output, 'background')
    
    #determines the path of the downloaded file to be processed  
    path = os.path.join(os.getcwd(), 'preprocessed')
    if (type == 1):
        path = os.path.join(path, 'story')
    elif (type == 2):
        path = os.path.join(path, 'background')
    
    # add the file name to the paths
    filepath = os.path.join(path, filename)
    output = os.path.join(output, filename)
    
    start = "0"
    
    if (type == 1):
        end = int(end[0:2])*60 + int(end[3:6])
    elif (type == 2):
        end = end
    
        
    probe_result=ffmpeg.probe(filepath)
    duration = probe_result.get("format",{}).get("duration",None)
    print(duration)
    
    input_stream = ffmpeg.input(filepath)
    
    pts = "PTS-STARTPTS"
    video = input_stream.trim(start = start, end = end).setpts(pts)
    audio = (input_stream
             .filter("atrim", start = start, end = end)
             .filter("asetpts", pts))
    
    video_and_audio = ffmpeg.concat(video, audio, v=1, a=1)
    
    if os.path.exists(output):
        os.remove(output)
    
    output = ffmpeg.output(video_and_audio, output, format="mp4")
    output.run()
    os.remove(filepath)
    