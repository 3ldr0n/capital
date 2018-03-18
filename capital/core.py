""" Edison Neto, This software is a text RPG based on the elder scrolls game series' lore.

Copyright (C) 2018 Edison Neto
This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public Licens
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

import os
import time
import pygame

import items
import enemies
from area import Area
from player import Player

background_music = os.getcwd() + '/music/morrowind.mp3'
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

    starting_area = Area("Prision")

    player = Player('Eldron')
    player.get_item(items.SteelSword())

    print(player)
    player.check_inventory()


if __name__ == '__main__':
    run()
