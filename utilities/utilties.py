from multiprocessing import process
import os
import time
import pathlib
import random
from utilities import downloader, slicer, makevideo



def addBackground(url):
    temp = downloader.download(url, "background")
    return

def makeStoryVideo(url):
    # temp = downloader.download(url, "story")
    
    num_parts = countFiles(os.path.join(os.path.join(os.getcwd(), 'processed'), 'story'))
    
    bgOffset = countFiles(os.path.join(os.path.join(os.getcwd(), 'processed'), 'background'))
    # print(bgOffset)
    

    
    for i in range(num_parts):
        filename = "part " + str(i) + ".mp4"
        background = "background " + (str(random.randint(0, bgOffset-1))) + ".mp4"
        makevideo.layerVideos(os.path.join(os.path.join(os.path.join(os.getcwd(), 'processed'), 'story'), filename),
                              os.path.join(os.path.join(os.path.join(os.getcwd(), 'processed'), 'background'), background))
        time.sleep(1)
    
    return
    
def clearPreprocessedBackgrounds():
    os.remove(os.path.join(os.path.join(os.getcwd(), 'preprocessed'), 'background'))
    return

def countFiles(dir):
    initial_count = 0
    for path in pathlib.Path(dir).iterdir():
        if path.is_file():
            initial_count += 1

    print(initial_count)
    return initial_count