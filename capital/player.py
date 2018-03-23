"""
Edison Neto, This software is a text RPG based on the elder scrolls' lore.

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

import items

class Player:

    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.maxhp = 100
        self.mana = 100
        self.maxmana = 100
        self.inventory = [items.Septim(0)]
        self.vampirism = False,
        self.lycanthropy = False


    def set_hp(self, hp):
        self.hp = hp


    def set_maxhp(self, maxhp):
        self.maxhp = maxhp


    def check_inventory(self):
        for item in self.inventory:
            print(item)


    def is_alive(self):
        return self.hp > 0


    def get_item(self, item):
        self.inventory.append(item)


    def acquire_vampirism(self):
        # TODO
        # Make player weak in the sun.
        self.vampirism = True


    def __str__(self):
        return "You are {}, you have {} points of health\n{} points of mana".format(
                                                self.name, self.hp, self.mana)


class Redguard(Player):

    def __init__(self):
        super().__init__('Redguard')


class Khajhit(Player):

    def __init__(self):
        super().__init__('Khajhit')
