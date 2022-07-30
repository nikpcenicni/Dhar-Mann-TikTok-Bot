import os
import re
from pytube import YouTube
from utilities import slicer


creator = "Dhar Mann"

def download(url: str, type: str):
    
    outpath = None
    # detemine if the video url is a background video or a story video
    if type == "story":
        outpath = os.path.join(os.path.join(os.getcwd(), 'preprocessed'), 'story')
    elif type == "background":
        outpath = os.path.join(os.path.join(os.getcwd(), 'preprocessed'), 'background')
        
    # ensure the url isnt empty
    if (url is None):
        return None
    
    # trys to download the video and saves to the preprocessed folder under the type folder
    try :
        yt = YouTube(url)
        name = yt.title
        stream = yt.streams.get_by_itag(22)
        name = re.sub('[^A-Za-z0-9]+', '', name)
        name = name.replace("| Dhar Mann ", "")
        name = name+".mp4"

        stream.download(
            output_path=outpath,
            filename=name
        )
        if type == "story":
            slicer.removeOutro(name, getEndTimeStamp(url), type)
            name = os.path.join(os.path.join(os.path.join(os.getcwd(), 'preprocessed'), 'story'),name)
            slicer.splitVideoToChunks(name, type)
        elif type == "background":
            name = os.path.join(os.path.join(os.path.join(os.getcwd(), 'preprocessed'), 'background'),name)
            slicer.splitVideoToChunks(name, type)
        return name
    except Exception as e:
        print(e)
        return None
    
    
    
def getName(url: str):
    yt = YouTube(url)
    return yt.title

def getEndTimeStamp(url: str):
    yt = YouTube(url)
    description = yt.description
    
    offset = description.find("CHAPTERS:")
    offset+= len("CHAPTERS:") + 8 + len(getName(url)) - 10
    
    time = description[offset:offset+5]
    
    print(time)
    return time

def getFileName(name: str):
    return name+".mp4"
