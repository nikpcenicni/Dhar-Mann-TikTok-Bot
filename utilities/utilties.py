import os
import time
import pathlib
from utilities import downloader, slicer, makevideo



def addBackground(url):
    temp = downloader.download(url, "background")
    return

def makeStoryVideo(url):
    temp = downloader.download(url, "story")
    num_parts = countFiles(os.path.join(os.path.join(os.getcwd(), 'processed'), 'story'))
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