#video downloader
from pytube import Youtube as yt
link=input("provide your link:")
Youtube_link=yt(link)
print(Youtube_link.title)
videos=Youtube_link.streams.all
links=list(enumerate(videos))
yt.streams.filter(file_extension='mp4')
for i in links:
    print(i)