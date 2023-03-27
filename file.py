from pytube import YouTube
link = "https://www.youtube.com/watch?v=7zS4myjhWsY "

YouTube_1 = YouTube(link)
#print(YouTube_1.title) fortitle
#print(YouTube_1.thumbnail_url) for thumbnail

videos = YouTube_1.streams.all() # for all format
#for only audio  videos = youtube_1.streams.filter(only_audio=True)
vid = list(enumerate(videos))

for i in vid:
      print(i)
      
strm = int(input("enter : "))
videos[strm].download()

print('successfully')