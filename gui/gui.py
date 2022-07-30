from tkinter import  *
import os

from utilities import slicer, downloader, makevideo

def addBackground():
    input = inputtxt.get(1.0,"end-1c")
    print(input)
    
def makeStoryVideo():
    input = inputtxt.get(1.0,"end-1c")
    
def clearPreprocessedBackgrounds():
    os.rmtree(os.path.join(os.path.join(os.getcwd(), 'preprocessed'), 'background'))
    return

root = Tk()
root.geometry("750x500")
frame = Frame(root)
frame.pack()

leftframe = Frame(root)
leftframe.pack(side=LEFT)

rightframe = Frame(root)
rightframe.pack(side=RIGHT)

label = Label(frame, text = "")
label.pack()

numBackgrounds = Label(frame, text = "Number of Backgrounds: " + str(slicer.countFiles(os.path.join(os.path.join(os.getcwd(), 'processed'), 'background'))))
numBackgrounds.pack()

inputtxt = root.Text(frame,
                height = 5,
                width = 20)

inputtxt.pack()

button1 = Button(leftframe, text = "Add background video", command = addBackground())
button1.pack(padx = 3, pady = 3)
button2 = Button(rightframe, text = "Make TikTok", command = makeStoryVideo())
button2.pack(padx = 3, pady = 3)
button3 = Button(leftframe, text = "Clear preprocessed files", command = clearPreprocessedBackgrounds())")
button3.pack(padx = 3, pady = 3)

root.title("Dhar Mann TikTok Bot")
root.mainloop()
    
