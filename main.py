from pytube import YouTube
import os
import pandas as pd
import tqdm

def video(link):
    yt = YouTube(link)
    destination='lmao/'
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path=destination)
    # yt.streams.filter(only_audio=True).first().download(output_path=destination)

def playlist(link):
    purl = Playlist(link)
    print(f"Total number of videos/songs = {purl.length}")
    nameOfPlaylist = input("Please name your playlist")
    destination = f'{nameOfPlaylist}'

    for video in purl.videos:
        print(video.title)
        song = video.streams.filter(only_audio=True).first()
        song.download(output_path=destination)

def song(link,destination):
    yt = YouTube(link)
    yt.streams.filter(only_audio=True).last().download(output_path=destination)

def changeExtensions(destination):
    # get all the names in the destination folder
    filenames = next(os.walk(destination), (None, None, []))[2]  # [] if no file

    filenamesminusExtension = [filename.replace('.webm', '') for filename in filenames]
    print(filenames)
    print(filenamesminusExtension)

    for i,j in zip(filenames,filenamesminusExtension):
        os.rename(f"/workspace/youtube-downloader/Liked Music/{i}", f"/workspace/youtube-downloader/Liked Music/{j}.mp3") # change extensions

def main(file):
    #import CSV file as pandas dataframe
    df = pd.read_csv(file)
    songURL = (df[['Song URL']])
    # print(songURL.head())
    songString=df["Song URL"].values.astype(str) # converting dataframe to numpy arrays
    destination='Liked Music/' # destination of download

    count=1 # counter 
    for i in songString: # iterating through array list and passing it to song function (poorly named lmao)
        song(i,destination)
        print(f"Downloaded {count}/{len(songString)}")
        count+=1

    print("Download Complete")
    print("Changing extensions now")
    changeExtensions(destination)

main('music-library-songs.csv')