from cgitb import text
from logging import PlaceHolder
import tkinter as tk
from tkinter import ttk
import os
from turtle import title

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
    url = bginput
    utilties.addBackground(url)
    
def makeVideo(url):
    utilties.makeStoryVideo(url)
    
def init_placeholder(widget, placeholder_text):
    widget.placeholder = placeholder_text
    if widget.get() == "":
        widget.insert("end", placeholder_text)

    # set up a binding to remove placeholder text
    widget.bind("<FocusIn>", remove_placeholder)
    widget.bind("<FocusOut>", add_placeholder)
    
def remove_placeholder(event):
    placeholder_text = getattr(event.widget, "placeholder", "")
    if placeholder_text and event.widget.get() == placeholder_text:
        event.widget.delete(0, "end")
        
def add_placeholder(event):
    placeholder_text = getattr(event.widget, "placeholder", "")
    if placeholder_text and event.widget.get() == "":
        event.widget.insert(0, placeholder_text)

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
    init_placeholder(bgInput, "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    bgInput.pack()
    addBgBut = ttk.Button(backgrounds,text="Add background", command=lambda: addBackground(url))
    addBgBut.pack()
    
    root.mainloop()
    
    
        
