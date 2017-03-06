# -*- coding: utf-8 -*-

import os, random
import pygame
from time import sleep
import RPi.GPIO as GPIO
from sys import exit

# this is where the music lives
music_dir = '/home/pi/Music/'

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


# this loop runs every half second and checks for button presses
# it also checks if the music is playing and plays the next song
# when the current song ends.

while True:

    try:

        # if music not playing, play a random song
        if (not pygame.mixer.music.get_busy()):

            play_random_song()
        
        # if random button play a random song    

            play_random_song()

        # if play/pause button is pressed

            # if the music is playing, pause
            if (pygame.mixer.music.get_busy()):
                pygame.mixer.music.pause()
            # else play
            else:
                pygame.mixer.music.unpause()
        
        # wait half a second    
        sleep(0.5)

    except KeyboardInterrupt:
        # kill the program if the user hits ctrl+c
        exit()
