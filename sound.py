from pygame import mixer
import time
import random

'''def music():
    musicList=["spongebob.ogg", "i_hate_people.ogg", "krabs_counting_money.ogg", "all_that_theme_song.ogg", "danny_phantom.ogg", "drake_and_josh.ogg",
     "fairly_oddparents.ogg", "hey_arnold.ogg", "iCarly.ogg", "jimmy_neutron.ogg", "kenan_and_kel.ogg", "rugrats.ogg", "spongebob_theme.ogg",
     "teenage_robot.ogg", "victorious.ogg", "zoey101.ogg"]

    # for choosing a random song in the list

    r = random.randint(0,len(musicList) - 1)

    mixer.init()
    mixer.music.load("./sound/" + musicList[r])
    mixer.music.play()
    i = len(musicList)
    j = 0
    for j in range (0,100):
        r = random.randint(0,len(musicList) - 1)
        mixer.music.queue("./sound/" + musicList[r])
        print()'''

musicList = ["spongebob.ogg", "i_hate_people.ogg", "krabs_counting_money.ogg", "all_that_theme_song.ogg", "danny_phantom.ogg", "drake_and_josh.ogg",
 "fairly_oddparents.ogg", "hey_arnold.ogg", "iCarly.ogg", "jimmy_neutron.ogg", "kenan_and_kel.ogg", "rugrats.ogg", "spongebob_theme.ogg",
 "teenage_robot.ogg", "victorious.ogg", "zoey101.ogg"]
currSong = None

def music():
    global currSong, musicList
    queueSong = random.choice(musicList)
    while queueSong == currSong:
        queueSong = random.choice(musicList)
    currSong = queueSong
    mixer.music.load("./sound/" + queueSong)
    mixer.music.set_volume(0.3)
    mixer.music.play()
