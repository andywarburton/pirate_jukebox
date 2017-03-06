# -*- coding: utf-8 -*-

import os, random
import pygame
from time import sleep
import RPi.GPIO as GPIO
from sys import exit

# this is where the music lives
music_dir = '/home/pi/Music/'

# configure the GPIO stuff
#GPIO.setmode(GPIO.BCM) 
#GPIO.setup(21, GPIO.IN)
#GPIO.setup(23, GPIO.IN)

# get the music thing going
pygame.init()
pygame.mixer.init()

# get list of files in music_dir
files = [ f for f in os.listdir(music_dir) if os.path.isfile(os.path.join(music_dir,f)) and f.endswith('.mp3') ]




# this function gets a random song from the 
# music directory and plays it

song = random.choice(files)
    
print song
    
song = music_dir + song

print song

# load the song
pygame.mixer.music.load(song)
    
# play the song
pygame.mixer.music.play(1)

while pygame.mixer.music.get_busy() == True:
    continue



