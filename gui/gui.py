from audioop import add
from cgitb import text
from logging import PlaceHolder
from re import S
import tkinter as tk
from tkinter import ttk
import os
from turtle import st, title

from utilities import slicer, downloader, makevideo, utilties

# def addBackground():
#     input = inputtxt.get(1.0,"end-1c")
#     print(input)
    
# def makeStoryVideo():
#     input = inputtxt.get(1.0,"end-1c")
    
# def clearPreprocessedBackgrounds():
#     os.rmtree(os.path.join(os.path.join(os.getcwd(), 'preprocessed'), 'background'))
#     return

def addBackground(bginput):
    url = bginput.get()
    utilties.addBackground(url)
    
def makeVideo(url):
    url = url.get()
    utilties.makeStoryVideo(url)


def gui():
    root = tk.Tk()
    root.geometry("750x500")
    root.title("Dhar Mann TikTok Bot")
    root.resizable(0, 0)
    
    root.rowconfigure(0, weight=4)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(1, weight=2)
    root.columnconfigure(1, weight=2)
    
    
    bgFrame = ttk.Frame(root)
    bgFrame.pack()
    
    backgrounds = ttk.Frame(bgFrame, width=250, height=250)
    backgrounds.pack()
    
    bgLabel = ttk.Label(backgrounds, text="Backgrounds")
    bgLabel.pack()
    
    numBg = ttk.Label(backgrounds, text="Number of backgrounds: " + str(len(os.listdir(os.path.join(os.getcwd(), 'processed', 'background')))))
    numBg.pack()
    
    url = tk.StringVar()
    bgInput = ttk.Entry(backgrounds, textvariable=url)
    bgInput.pack()
    addBgBut = ttk.Button(backgrounds,text="Add background", command=lambda: addBackground(url))
    addBgBut.pack()
    
    storysFrame = ttk.Frame(root)
    storysFrame.pack()
    
    storys = ttk.Frame(storysFrame, width=250, height=250)
    storys.pack()
    
    storysLabel = ttk.Label(storys, text="Storys")
    storysLabel.pack()
    
    storyURL = tk.StringVar()
    storyInput = ttk.Entry(storys, textvariable=storyURL)
    storyInput.pack()
    
    addStoryBut = ttk.Button(storys,text="Add story", command=lambda: makeVideo(storyURL))
    addStoryBut.pack()
    
    
    
    
    
    
    root.mainloop()
    
    
        
