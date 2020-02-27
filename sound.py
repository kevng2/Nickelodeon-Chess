from pygame import mixer
import time

def music():
    mixer.init()
    mixer.music.load("spongebob.mp3")
    mixer.music.play()
