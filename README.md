# Pi-JukeBox

A simple MP3 player for Pimoroni's Pirate Radio kit for the Raspberry Pi Zero W.

My 6 year old son wanted a way to listen to music in his room and I felt a full hi-fi system was OTT for his needs (and simple speaker systems these days all require a connected music player or bluetooth device - again, total overkill). So I grabbed a Pirate Radio kit from Pimoroni and created this simple script to randomly play any music we upload to the Raspberry Pi over SFTP.

## Requirements:

This script requires Python 3, Pygame and Pimoroni's PhatBeat Library

To install Python 3 and Pygame follow these directions:

```
$ sudo apt-get install libsdl-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev 
$ sudo apt-get install libsmpeg-dev libportmidi-dev libavformat-dev libswscale-dev
$ sudo apt-get install python3-dev python3-numpy
$ sudo apt-get install python-pygame

$ python3 setup.py build 
$ sudo python3 setup.py install
```

Instructions to install Pimoroni's PhatBeat library are here:

https://github.com/pimoroni/phat-beat (be sure to install the Python 3 version)

## Time to Jam!

Put your music in the included `music` directory (only MP3's are supported right now).

Once this is up and running you can run the script with

`sudo python ./pirate_jukebox.py`

To make it launch on startup, follow the instructions here:

http://www.instructables.com/id/Raspberry-Pi-Launch-Python-script-on-startup/?ALLSTEPS

(the launcher.sh is already included in the project).

## Controls

FFWD: Play another song at random

Play/Pause: Does what it says on the tin

RRWD: Go back to the start of the current song

VOL UP: Does what it says on the tin

VOL DOWN: Tin, does what says on it.

## Thanks!

Thanks to Pimoroni for creating the awesome Pirate Radio hardware and example scripts that I built this on top of and the Pygame project!


