from turtle import width
from moviepy.editor import *
from moviepy.editor import VideoFileClip, clips_array, vfx, TextClip
from moviepy.audio.fx.all import volumex
import os
from utilities import utilties
def layerVideos(story_file, background_file, part_num):
    if (story_file is None or background_file is None):
        return None
    back = VideoFileClip(background_file)
    story = VideoFileClip(story_file)
    back = back.fx(volumex, 0.0)
    
    
    filename = os.path.join(os.path.join(os.getcwd(), 'Output'), ("Part " + str(utilties.countFiles(os.path.join(os.getcwd(),'Output')))  +".mp4"))
    
    txt_clip = TextClip(("part " + str(part_num)), fontsize = 75, color = 'blue') 
    
    # setting position of text
    txt_clip = txt_clip.set_pos('center').set_duration(10)
    
    bg = CompositeVideoClip([back, txt_clip])
    final = clips_array([[story.resize(width=720)], [bg.resize(width=720)]])
    
    #final = CompositeVideoClip([story.rotate(90).set_position((0,480))],[back.rotate(90).set_position((0,0))])
    final.write_videofile(filename)
    
    os.remove(story_file)

    