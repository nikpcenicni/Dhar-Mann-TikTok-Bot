from turtle import width
from moviepy.editor import *
from moviepy.editor import VideoFileClip, clips_array, vfx
from moviepy.audio.fx.all import volumex
import os
from utilities import utilties
def layerVideos(story_file, background_file):
    if (story_file is None or background_file is None):
        return None
    back = VideoFileClip(background_file)
    story = VideoFileClip(story_file)
    back = back.fx(volumex, 0.0)
    
    
    filename = os.path.join(os.path.join(os.getcwd(), 'Output'), ("part " + str(utilties.countFiles(os.path.join(os.getcwd(),'Output')))  +".mp4"))
    final = clips_array([[story.resize(width=720)], [back.resize(width=720)]])
    
    #final = CompositeVideoClip([story.rotate(90).set_position((0,480))],[back.rotate(90).set_position((0,0))])
    final.write_videofile(filename)
    
    os.remove(story_file)

    