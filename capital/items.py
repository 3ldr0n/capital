"""
Edison Neto, This software is a text RPG based on the elder scrolls game series' lore.

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

class Item:

    def __init__(self, name, descriptio, value):
        self.name = name
        self.description = description
        self.value = value


    def __str__(self):
        return "{}\n{}\nValue: {}".format(self.name, self.description, self.value)


class Septim(Item):

    def __init__(self, quantity):
        self.quantity = quantity
        super().__init__("Septims", "Septims are the moneyt", 1)


class Weapon(Item):

    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)


    def __str__(self):
        return "{}\n{}\nDamage: {}\nValue: {}".format(self.name,
                                                      self.description,
                                                      self.value, self.damage)


class Rock(Weapon):

    def __init__(self):
        super().__init__(
                         name="Rock",
                         description="Rocky rock",
                         value=0,
                         damage=3)


class BluntSword(Weapon):

    def __init__(self):
        super().__init__(
                         name="Blunt Sword",
                         description="Just a blunt sword",
                         value=5,
                         damage=8)


class RustySword(Weapon):

    def __init__(self):
        super().__init__(
                         name="Rusty Sword",
                         description="Rusty sword",
                         value=10,
                         damage=15)


class SteelSword(Weapon):

    def __init__(self):
        super().__init__(
                         name="Steel Sword",
                         description="A sword made out of steel",
                         value=15,
                         damage=18)
