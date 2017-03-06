# -*- coding: utf-8 -*-

import os, random
import pygame
import time
import RPi.GPIO as GPIO
from sys import exit

# this is where the music lives
music_dir = '/home/pi/Music/'
music_is_paused = 0

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# get the music thing going
pygame.init()
pygame.mixer.init()

# get list of files in music_dir
files = [ f for f in os.listdir(music_dir) if os.path.isfile(os.path.join(music_dir,f)) and f.endswith('.mp3') ]

# this function gets a random song from the
# music directory and plays it

def play_random_song():

    song = random.choice(files)

    print song

    song = music_dir + song

    # load the song
    pygame.mixer.music.load(song)

    # play the song
    pygame.mixer.music.play(1)


while True:
    random_button = GPIO.input(23)
    playpause_button = GPIO.input(24)

    if random_button == False:

        play_random_song()
        time.sleep(1)

    if playpause_button == False:

        print pygame.mixer.music.get_busy()

        if (music_is_paused == 0):
            pygame.mixer.music.pause()
            music_is_paused = 1
            print('pause')
        else:
            pygame.mixer.music.unpause()
            music_is_paused = 0
            print('play')
        time.sleep(1)
