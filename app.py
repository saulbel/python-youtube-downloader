from pytube import YouTube

location = './'

# input
def getInput():
    link = input ("Introduce the link of Youtube you wanna download or 'exit' to close the app: ")
    if link.upper() == 'EXIT':
        return link
    else:
        yt = YouTube(link)
        return yt


# details
def getDetails(yt):
    print("Title: ", yt.title)
    print("Views: ", yt.views)
    print("Length: ", yt.length)


# choose download format
download_format = ''
while download_format.upper() != 'EXIT':
    yt = getInput()
    if isinstance(yt, str):
        print ("Till nex time !")
        break
    else:
        getDetails(yt)
        download_format = input ("Introduce 'video' ,'audio', or 'exit': ")
        if download_format.upper() == 'VIDEO':
            print ("Downloading....")
            ys = yt.streams.get_highest_resolution()
            ys.download(location)
            print ("Download completed")
        elif download_format.upper() == 'AUDIO':
            print ("Downloading....")
            ys = yt.streams.get_audio_only()
            ys.download(location)
            print ("Download completed")
        elif download_format.upper() == 'EXIT':
            print ("Till nex time !")
        else:
            print ("Please, introduce the words 'video', 'audio', or 'exit': ")
