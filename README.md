# Pi-JukeBox
A simple MP3 player for my Raspberry Pi

This is a personal project to play random MP3 files from a directory using a python script with simple button controls via GPIO. The \_working file does work at the moment but is kinda Janky. Obviously no MP3 files are included because copyright is a pain in the bum.

This script requires Python 3 and Pygame.

To install Python 3 and Pygame follow these directions:

```$ sudo apt-get install mercurial 
$ hg clone https://bitbucket.org/pygame/pygame
$ cd pygame

$ sudo apt-get install libsdl-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev 
$ sudo apt-get install libsmpeg-dev libportmidi-dev libavformat-dev libswscale-dev
$ sudo apt-get install python3-dev python3-numpy

$ python3 setup.py build 
$ sudo python3 setup.py install```
