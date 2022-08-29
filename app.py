from pytube import YouTube

# input
location = './'
link = input ("Introduce the link of Youtube you wanna download: ")
yt = YouTube(link)

# details
print("Title: ", yt.title)
print("Views: ", yt.views)
print("Length: ", yt.length)

# choose download format
download_format = ''
while download_format.upper() != 'EXIT':
    download_format = input ("Introduce 'video' for mp4, 'audio' for mp3 or 'exit' if you wanna finish downloading stuff: ")
    if download_format.upper() == 'VIDEO':
        print ("Downloading....")
        ys = yt.streams.get_highest_resolution()
        ys.download(location)
        print ("Downdload completed")
    elif download_format.upper() == 'AUDIO':
        print ("Downloading....")
        ys = yt.streams.get_audio_only()
        ys.download(location)
        print ("Downdload completed")
    elif download_format.upper() == 'EXIT':
        print ("Till nex time !")
    else:
        print ("Please, introduce the words 'video', 'audio' or 'exit'")
