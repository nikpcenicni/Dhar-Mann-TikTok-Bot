from multiprocessing import process
import os
import time
import pathlib
import random
from gui import gui
from utilities import downloader, slicer, makevideo
from threading import *



def addBackground(url):
    thread = Thread(target=downloader.download, args=(url, "background"))
    thread.setDaemon(True)
    thread.start()
    return

def addStory(url):
    thread = Thread(target=downloader.download, args=(url, "story"))
    thread.setDaemon(True)
    thread.start()
    return

def makeStoryVideo():
    gui.updateProgressBar(0, "Making Story Video")
    bgOffset = countFiles(os.path.join(os.path.join(os.getcwd(), 'processed'), 'background'))
    # print(bgOffset)
    if (bgOffset <= 0):
        print("No background videos found. Please download background videos first.")
        return
    
    num_parts = countFiles(os.path.join(os.path.join(os.getcwd(), 'processed'), 'story'))
    

    # print(bgOffset)
    
    
    offset = ((1/num_parts)/2) * 100
    threads=[]
    for i in range(num_parts):
        percent = calculateProgress(num_parts, i)*100+offset
        gui.updateProgressBar(percent, "Making part " + str(i+1) + " of " + str(num_parts))
        filename = "part " + str(i+1) + ".mp4"
        background = "background " + (str(random.randint(1, bgOffset-1))) + ".mp4"
        threads.append(Thread(target=makevideo.layerVideos, args=(os.path.join(os.path.join(os.path.join(os.getcwd(), 'processed'), 'story'), filename),
                              os.path.join(os.path.join(os.path.join(os.getcwd(), 'processed'), 'background'), background),(i+1))))
        threads[i].setDaemon(False)
        threads[i].start()
        gui.updateProgressBar(calculateProgress(num_parts, i+1), ("Finished Part " + str(i+1)))
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

def calculateProgress(num_parts, num_processed):
    progress = num_processed/num_parts
    return progress