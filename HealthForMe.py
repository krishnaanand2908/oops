import os
import pyttsx3
import datetime
import pygame
import time
import fontstyle as fnt

def musicPlayer(file, stopper):
    pygame.mixer.init()
    pygame.mixer.load(file)
    pygame.mixer.play()
    while True:
        user_input = input()
        if user_input == stopper:
            pygame.mixer.music.stop()
            break

def log(message):
    with open("MyActivityLog.txt", "a") as f:
        f.write(f"{message} {datetime.datetime.now()}\n")
        
if __name__ == "__main__":
    init_water = time.time()
    init_water = time.time()
    init_water = time.time()
    waterSecs = 30*60
    exerSecs = 40*60
    eyeSecs = 35*60
    
    while True:
        if (time() - init_water) > waterSecs:
            print(fnt.apply("Water Drinking time. Enter 'drank' to stop the alarm.", "blue/bold"))
            musicPlayer('water.mp3', 'drank')
            init_water = time()
            log("Drank Water at")
    
        if (time() - init_water) > waterSecs:
            print(fnt.apply("Water Drinking time. Enter 'drank' to stop the alarm.", "green/bold"))
            musicPlayer('eye.mp3', 'DoneEyes')
            init_water = time()
            log("Eyes relaxed at")
        

