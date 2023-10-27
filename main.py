# video downloader
from pytube import Youtube
link = input("provide your link:")
Youtube_link = yt(link)
print(Youtube_link.title)
videos = Youtube_link.streams.filter(progressive=True)
links = list(enumerate(videos))
for i in links:
    print(i)
stream = input("Provide the index you wanna download: ")
videos[stream].download()
print("Successfully Downloaded!")
