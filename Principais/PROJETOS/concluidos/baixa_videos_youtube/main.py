from pytubefix import YouTube


def Download(link: str):
    video = YouTube(link)
    video = video.streams.filter(progressive=True).first()
    video.download()


Download("https://www.youtube.com/watch?v=5s2urYqLjjM&t=18s")
