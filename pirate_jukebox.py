#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, random
import pygame
import time
from sys import exit
import signal
import phatbeat

print("""
==============================
Pirate Jukebox! Lets do this!!
==============================

CTRL+C to quit
------------------------------
""")

# this is where the music lives
music_dir = './music/'
music_is_paused = 0
music_playing = 0

# get the music thing going
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
pygame.mixer.init()
pygame.mixer.music.set_volume(0.5)
volume = 0.5

# get list of files in music_dir
files = [ f for f in os.listdir(music_dir) if os.path.isfile(os.path.join(music_dir,f)) and f.endswith('.mp3') ]

# this function gets a random song from the
# music directory and plays it

def play_song(song):

    # load the song
    pygame.mixer.music.load(song)

    # play the song
    pygame.mixer.music.play(1)

    # remember we have muisc
    global music_playing
    music_playing = song

    print(song)

def play_random_song():
    song = random.choice(files)
    song = music_dir + song
    play_song(song)

## buttons wot do stuff

## Fast Forward Button
@phatbeat.on(phatbeat.BTN_FASTFWD)
def fast_forward(pin):
    play_random_song()
    time.sleep(1)

## Play / Pause Button
@phatbeat.on(phatbeat.BTN_PLAYPAUSE)
def play_pause(pin):

    global music_playing
    global music_is_paused

    if(music_playing == 0):
        play_random_song()
        time.sleep(1)

    if (music_is_paused == 0):
        pygame.mixer.music.pause()
        music_is_paused = 1
    else:
        pygame.mixer.music.unpause()
        music_is_paused = 0
    time.sleep(1)

## Volume Up Button
@phatbeat.on(phatbeat.BTN_VOLUP)
def volume_up(pin):
    global volume
    if(volume < 1):
        volume = volume + 0.1
        pygame.mixer.music.set_volume(volume);

## Volume Down Button
@phatbeat.on(phatbeat.BTN_VOLDN)
def volume_down(pin):
    global volume
    if(volume > 0.1):
        volume = volume - 0.1
        pygame.mixer.music.set_volume(volume);

## Rewind Button
@phatbeat.on(phatbeat.BTN_REWIND)
def rewind(pin):
    play_song(music_playing)


## lets keep python paying attention by looping forever
## this little loops keeps music playing when one song ends
try:
    while True:
        # play some music if none is playing
        if(pygame.mixer.music.get_busy() == 0):
            play_random_song()

except KeyboardInterrupt:
    # kill the jukebox if the user hits ctrl+c
    print("""
==============================
Pirate Jukebox! OUT!
==============================
    """)
    exit()
