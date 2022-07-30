from moviepy.editor import *
from moviepy.editor import VideoFileClip, clips_array, vfx
from moviepy.audio.fx.all import volumex

def layerVideos(story_file, background_file):
    if (story_file is None or background_file is None):
        return None
    back = VideoFileClip(background_file)
    story = VideoFileClip(story_file)
    back = back.fx(volumex, 0.4)
    
    final = clips_array([[story.resize(0.40)], [back.resize(1.20)]])
    
    #final = CompositeVideoClip([story.rotate(90).set_position((0,480))],[back.rotate(90).set_position((0,0))])
    final.write_videofile("output-1.mp4")
    