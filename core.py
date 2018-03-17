import os
import time
import pygame

from area import Area

background_music = os.getcwd() + '/morrowind.mp3'
def play_background_music():
    pygame.mixer.init()
    pygame.mixer.music.load(background_music)
    pygame.mixer.music.play()

play_background_music()

def opening():
    columns = os.get_terminal_size().columns

    text = open('opening_text.txt', 'r')
    opening_text = text.readlines()

    for line in opening_text:
        print(line.center(columns))
        time.sleep(3)

def choice():
    choice = ""
    while choice not in possible_choices:
        choice = input("> ")
    return choice


def run():
    opening()

    starting_area= Area("Prision")

if __name__ == '__main__':
    run()
