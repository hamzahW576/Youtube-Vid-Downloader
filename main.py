
from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

# Test
print("Title: ", yt.title)
print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('/Users/hamzahweldingwala/Downloads/')
