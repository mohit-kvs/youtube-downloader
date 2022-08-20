from pytube import YouTube
import os

def video(link):
    yt = YouTube(link)
    destination='lmao/'
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path=destination)
    # yt.streams.filter(only_audio=True).first().download(output_path=destination)

def playlist(link):
    # p = input("Enter th url of the playlist")
    purl = Playlist(link)
    print(f"Total number of videos/songs = {purl.length}")
    nameOfPlaylist = input("Please name your playlist")
    destination = f'{nameOfPlaylist}'

    for video in purl.videos:
        print(video.title)
        song = video.streams.filter(only_audio=True).first().download(output_path=destination)
        #video.streams.first().download()


def main():
    link='https://www.youtube.com/watch?v=WN7nBZMB3lk'
    video(link)

main()