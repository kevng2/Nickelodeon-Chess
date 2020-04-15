from pygame import mixer
import time

def music():
    mixer.init()
    mixer.music.load("spongebob.ogg")
    mixer.music.play()
