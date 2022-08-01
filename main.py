from utilities import downloader
from utilities import slicer
from utilities import utilties, makevideo
from gui import gui
import pathlib
import os



print(
    """
┌───┬┐        ┌─┐┌─┐          ┌────┬┐┌────┐ ┌┐   ┌──┐   ┌┐
└┐┌┐││        ││└┘││          │┌┐┌┐│││┌┐┌┐│ ││   │┌┐│  ┌┘└┐
 ││││└─┬──┬─┐ │┌┐┌┐├──┬─┐┌─┐  └┘││├┤│├┤││├┴─┤│┌┐ │└┘└┬─┴┐┌┘
 ││││┌┐│┌┐│┌┘ ││││││┌┐│┌┐┤┌┐┐   ││├┤└┘┘│││┌┐│└┘┘ │┌─┐│┌┐││
┌┘└┘││││┌┐││  ││││││┌┐│││││││   ││││┌┐┐│││└┘│┌┐┐ │└─┘│└┘│└┐
└───┴┘└┴┘└┴┘  └┘└┘└┴┘└┴┘└┴┘└┘   └┘└┴┘└┘└┘└──┴┘└┘ └───┴──┴─┘

"""
)

#print(pathlib.Path(__file__).parent.resolve())



# url = input("Enter a YouTube URL for : ")

# type = input("Enter 1 for story video or 2 for background video : ")

#url = "https://www.youtube.com/watch?v=cJ03M8FYhd4"
#url = "https://www.youtube.com/watch?v=6RFoWha_62k"
#url = "https://www.youtube.com/watch?v=CCPQ_WU9aGQ"

#url = "https://www.youtube.com/watch?v=7YZ3AyqGyLc"
#url = "https://www.youtube.com/watch?v=NJEqifBtNOw"

#print(downloader.getEndTimeStamp(url))

#downloader.download(url, int(type))
back = os.path.join(os.path.join(os.getcwd(), 'processed'), 'background')
back = os.path.join(back, "background 0.mp4")

#type = "background"

story = os.path.join(os.path.join(os.getcwd(), 'processed'), 'story')
story = os.path.join(story, "SisterAshamedOfHerDisabledBrotherSheInstantlyRegretsItDharMann_0_180.mp4")

type = "story"

#slicer.layerVideos(story, back)

#slicer.splitVideoToChunks("SisterAshamedOfHerDisabledBrotherSheInstantlyRegretsItDharMann.mp4", type)

#makevideo.layerVideos(story, back)

url = 'https://www.youtube.com/watch?v=tdulthFSkjQ'

#utilties.addBackground(url)

gui.gui()
#url = "https://www.youtube.com/watch?v=bpfQ8-UYt3g"
#utilties.makeStoryVideo(url)

# makevideo.layerVideos(story, back)


# title = downloader.getName(url)
# inputfile = os.path.join(os.path.join(os.path.join(os.getcwd(), 'preprocessed'), 'story'), title + '.mp4')

# slicer.split_cut(inputfile, 60)
