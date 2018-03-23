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

    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value


    def __str__(self):
        return "{}\n{}\nValue: {}".format(self.name, self.description, self.value)


class Septim(Item):

    def __init__(self, quantity):
        self.quantity = quantity
        super().__init__("Septims", "Septims are the money.", 1)


class Weapon(Item):

    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)


    def enhance(self, percentage):
        self.damage += (self.damage * percentage)


    def __str__(self):
        return "{}\n{}\nDamage: {}\nValue: {}".format(self.name,
                                                      self.description,
                                                      self.value, self.damage)

class IronSword(Weapon):

    def __init__(self):
        super().__init__(
                         name="Iron Sword",
                         description="A sword made out of iron.",
                         value=10,
                         damage=15)

class SteelSword(Weapon):

    def __init__(self):
        super().__init__(
                         name="Steel Sword",
                         description="A sword made out of steel",
                         value=15,
                         damage=18)


class EbonySword(Weapon):

    def __init__(self):
        super().__init__(
                         name="Ebony Sword",
                         description="A sword made out of ebony",
                         value=35,
                         damage=40)
