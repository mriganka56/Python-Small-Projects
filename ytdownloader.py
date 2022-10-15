from pytube import YouTube
yt=YouTube("https://www.youtube.com/watch?v=WDxkBjL_r8g")

x=yt.streams.filter(file_extension="mp4")
y=x.get_by_resolution("720p")
y.download("E:\Affiliate Marketing")