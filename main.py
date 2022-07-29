from operator import concat
from utilities import downloader
from utilities import slicer
import pathlib
import os



print(
    """
┌───┬┐░░░░░░░┌─┐┌─┐░░░░░░░░░┌────┬┐┌────┐░┌┐░░┌──┐░░░┌┐░
└┐┌┐││░░░░░░░││└┘││░░░░░░░░░│┌┐┌┐│││┌┐┌┐│░││░░│┌┐│░░┌┘└┐
░││││└─┬──┬─┐│┌┐┌┐├──┬─┐┌─┐░└┘││├┤│├┤││├┴─┤│┌┐│└┘└┬─┴┐┌┘
░││││┌┐│┌┐│┌┘││││││┌┐│┌┐┤┌┐┐░░││├┤└┘┘│││┌┐│└┘┘│┌─┐│┌┐││░
┌┘└┘││││┌┐││░││││││┌┐│││││││░░││││┌┐┐│││└┘│┌┐┐│└─┘│└┘│└┐
└───┴┘└┴┘└┴┘░└┘└┘└┴┘└┴┘└┴┘└┘░░└┘└┴┘└┘└┘└──┴┘└┘└───┴──┴─┘

"""
)

print(pathlib.Path(__file__).parent.resolve())



# url = input("Enter a YouTube URL for : ")

# type = input("Enter 1 for story video or 2 for background video : ")

#url = "https://www.youtube.com/watch?v=cJ03M8FYhd4"
#url = "https://www.youtube.com/watch?v=6RFoWha_62k"
url = "https://www.youtube.com/watch?v=CCPQ_WU9aGQ"
type = "2"

#print(downloader.getEndTimeStamp(url))

downloader.download(url, int(type))



# title = downloader.getName(url)
# inputfile = os.path.join(os.path.join(os.path.join(os.getcwd(), 'preprocessed'), 'story'), title + '.mp4')

# slicer.split_cut(inputfile, 60)
