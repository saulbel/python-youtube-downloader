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
- What if we wanna extract the video from the container to our local machine? It's quite simple, we just need the `container id`:
````
$ docker ps
CONTAINER ID   IMAGE                       COMMAND   CREATED         STATUS         PORTS     NAMES
0589c906c96c   python-youtube-downloader   "sh"      6 minutes ago   Up 6 minutes             bold_babbage
$ docker cp 0589c906c96c:/app/'Dance With The Dead - Andromeda [Synthwave  Cyberpunk) (The 80s Guy Montage).mp4' video_downloaded.mp4
$ ls -lrth
-rw-r--r--  1 saul saul  55M Aug 29 19:35 video_downloaded.mp4
````
- What if I told you that you can map your current folder and the docker volume so you do not have to extract the video from the container? Let's do it.
````
$ docker run -it -v ${PWD}:/app python-youtube-downloader sh
CONTAINER ID   IMAGE                       COMMAND   CREATED         STATUS         PORTS     NAMES
0589c906c96c   python-youtube-downloader   "sh"      6 minutes ago   Up 6 minutes             bold_babbage
# ls
Dockerfile  README.md  app.py  requirements.txt  scripts
# python3 app.py
Introduce the link of Youtube you wanna download: https://www.youtube.com/watch?v=Oa_joiuHRmo&ab_channel=SxDementia
Title:  ROCKY - Retrospective (2016)
Views:  4466358
Length:  636
Introduce 'video' for mp4, 'audio' for mp3 or 'exit' if you wanna finish downloading stuff: video
Downloading....
Downdload completed
Introduce 'video' for mp4, 'audio' for mp3 or 'exit' if you wanna finish downloading stuff: exit
Till nex time !
# exit
$ ls
Dockerfile   README.md  'ROCKY - Retrospective (2016).mp4'   app.py   requirements.txt   scripts
````
## GitHub Actions
I have built a CI pipeline that builds a custom `python` docker image with `Dockerfile` and pushes it into GitHub container registry  `ghcr.io`. If I want to pull new `docker image` I will just have to:
````
$ docker pull ghcr.io/saulbel/python-youtube-downloader:main
$ docker images
REPOSITORY                                  TAG                 IMAGE ID       CREATED             SIZE
ghcr.io/saulbel/python-youtube-downloader   main                a6219a03e4e5   3 minutes ago       74.4MB
````
