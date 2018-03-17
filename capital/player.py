# -*- coding: utf-8 -*-

import items

class Player:

    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.maxhp = 100
        self.inventario = [items.Septim(15)]

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
        self.inventario.append(item)
