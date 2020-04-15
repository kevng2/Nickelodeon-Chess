from pygame import mixer
import time
import random

def music():
    musicList = ["spongebob.ogg", "i_hate_people.ogg", "krabs_counting_money.ogg"]

    # for choosing a random song in the list
    r = random .randint(0,2)

    mixer.init()
    mixer.music.load("./sound/" + musicList[r])
    mixer.music.play()
