from pygame import mixer
from datetime import datetime
from time import time
def logs(msg):
    with open("mylogs.txt", "a")as f:
        f.write(f"{msg} {datetime.now()}\n")

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a == stopper :
            mixer.music.stop()
            break
        else:
            mixer.music.play()
if __name__=='__main__':
    init_water=time()
    init_eyes=time()
    init_exer=time()
    watersecs=1800 #Every 30 mins
    eyessecs=2400 #Every 40 mins
    exersecs=2700 #Every 45 mins
    while True:
        if time() - init_water > watersecs:
            print("Time to drink Water , Type 'Drank' to stop the alarm")
            musiconloop("water-filled-cup-9901.mp3","drank")
            init_water=time()
            logs("Drank Water At ")
        elif time() -init_eyes > eyessecs:
            print("Time for eyes exercise, Type 'EyDone' to stop the alarm")
            musiconloop("heart-beat-6797.mp3","EyDone")
            init_eyes=time()
            logs("Eyes Exercise Done At ")
        elif time() -init_exer > exersecs:
            print("Time for some Physical Activity , Type 'ExDone' to stop the alarm")
            musiconloop("heavy-breathing-14431.mp3","ExDone")
            init_exer=time()
            logs("Physical Activities Done At ")

