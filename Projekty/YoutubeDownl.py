from pytube import YouTube

link = ("https://www.youtube.com/watch?v=EAYlckSaviI")
yt = YouTube(link)
video = yt.streams.all()
vid = list(enumerate(video))
for i in vid:
    print (i)
print()

strm = int(input("enter:"))
video[strm].download()
print("Succesull")
