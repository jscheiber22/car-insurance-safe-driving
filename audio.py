import pygame
from time import sleep

class Audio:
    def __init__(self):
        file_location = 'beep.mp3'
        pygame.mixer.pre_init(frequency=48000, buffer=2048)
        pygame.mixer.init()
        pygame.mixer.music.load(file_location)

    
    def alert(self):
        pygame.mixer.music.play()