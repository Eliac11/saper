import os
import pygame 

def runmusic():
    pygame.init()
    #os.system('start mu\win.wav')

    pygame.mixer.music.load('mu\win.mp3')
    pygame.mixer.music.play()
    pygame.time.wait(20000)
    pygame.mixer.music.stop()

#runmusic()
def STOP():
    pygame.mixer.music.stop()