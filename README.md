# Python-youtube-downloader
## Prerequisites
* `Docker`

## Project structure
```
python-youtube-downloader
|── app.py
|── Dockerfile    
└── scripts
     └── setup.sh
```
## Tasks to accomplish
- Create a simple youtube video downloader app using `Python`.
- Use `Docker` to avoid installing `Python` on our machine.

## How to install the tools
I have included a custom script `setup.sh` that allows you to install `docker` on `Debian`.
I recommend to download it and change it with your `username` because I have decided to add my `user` to `docker group`. It is a good practice to run docker with a user instead of as `root`.

## How to setup this project locally
- First we should download it with either `git clone` or as `.zip`.
- Then we will modify `/scripts/setup.sh` with our `username` and we will execute it.

## First task: create the application
- We are gonna use `pytube` library because it has everything that we need. The app is really simple, it just ask for a `youtube video url` and it gives us the choice of downloading the video or just the audio.

## Second task: create the Dockerfile
- The idea of using `Docker` is to avoid installing `Python` on our machine. So we are gonna create a custom `docker-image`:
````
docker build . -t python-youtube-downloader
````
- Now we can list our `docker-image`:
````
$ docker images
REPOSITORY                             TAG                       IMAGE ID       CREATED              SIZE
python-youtube-downloader              latest                    15dc98a47ba8   About a minute ago   161MB
````
- Finally we can access run and access our docker container:
````
$ docker run -it python-youtube-downloader sh
````
- Now we will just have to execute our program and download as many videos as we want to :)
````
# python3 app.py
Introduce the link of Youtube you wanna download: https://www.youtube.com/watch?v=ICuM2o-Vcms&ab_channel=The%2780sGuy
Title:  Dance With The Dead - Andromeda [Synthwave / Cyberpunk) (The '80s Guy Montage)
Views:  851523
Length:  300
Introduce 'video' for mp4, 'audio' for mp3 or 'exit' if you wanna finish downloading stuff: video
Downloading....
Downdload completed
Introduce 'video' for mp4, 'audio' for mp3 or 'exit' if you wanna finish downloading stuff: exit
Till nex time !
````