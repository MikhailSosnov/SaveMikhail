# from ggts import gTTS
# import pygame
import pyttsx3
engine = pyttsx3.init()
# engine.say('Афанасий')
# engine.runAndWait()

with open('song_Afonas.txt') as f:
    for line in f:
        print(line, end='')
        engine.say(line)
        engine.runAndWait()