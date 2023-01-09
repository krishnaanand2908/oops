import os
import datetime
import pygame
import time
import fontstyle as fnt

def musicPlayer(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while True:
        user_input = input(fnt.apply('Press Enter to stop: '))
        if user_input == '':
            pygame.mixer.music.stop()
            break


if __name__ == '__main__':
    os.system('cls')
    while True:
        hour = int(input(fnt.apply('Input Hour: ', 'blue/bold')))
        minute = int(input(fnt.apply('Input Minute: ', 'blue/bold')))
        second = int(input(fnt.apply('Input Second: ', 'blue/bold')))
        sec = (hour*60*60) + (minute*60) + (second)
        init_timer = time.time()
        while True:
            if (time.time() - init_timer) == sec:
                musicPlayer('timer.mp3')
                init_timer = time.time()
                break