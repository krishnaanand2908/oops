import os
import datetime
import pygame
import time
import fontstyle as fnt

def musicPlayer(file, stopper):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while True:
        user_input = input()
        if user_input == stopper:
            pygame.mixer.music.stop()
            break

def log(message):
    with open("MyActivityLog.txt", "a") as f:
        f.write(f"{message} {datetime.datetime.now()}\n")
        
if __name__ == "__main__":
    os.system('cls')
    init_water = time.time()
    init_eyes = time.time()
    init_exercise = time.time()
    waterSecs = 30*60
    exerSecs = 35*60
    eyeSecs = 40*60
    
    while True:
        if (time.time() - init_water) > waterSecs:
            print(fnt.apply("Water Drinking time. Enter 'done' to stop the alarm.", "blue/bold"))
            musicPlayer('water.mp3', 'done')
            init_water = time.time()
            log("Drank Water at")
    
        if (time.time() - init_eyes) > eyeSecs:
            print(fnt.apply("Eyes Relaxation time. Enter 'done' to stop the alarm.", "green/bold"))
            musicPlayer('eyes.mp3', 'done')
            init_water = time.time()
            log("Eyes relaxed at")
            
        if (time.time() - init_exercise) > exerSecs:
            print(fnt.apply("Physical Activity time. Enter 'done' to stop the alarm.", "yellow/bold"))
            musicPlayer('exercise.mp3', 'done')
            init_water = time.time()
            log("Physical Activity done at")
        

