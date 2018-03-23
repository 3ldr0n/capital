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

from utils import select_race

class Enemy:

    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage


class Draugr(Enemy):

    def __init__(self):
        super().__init__(name="Draugr", hp=100, damage=20)


class Vampire(Enemy):

    def __init__(self, race):
        self.race = race
        super().__init__(name="Vampire", hp=170, damage=65)


    def vampirism(self, player):
        player.acquire_vampirism()


class Bandit(Enemy):

    def __init__(self, name, hp, damage, race):
        self.race = race
        super().__init__(name, hp, damage)


class BanditChied(Bandit):

    def __init__(self):
        super().__init__("Bandit Chief", 200, 75, select_race())


class Mage(Enemy):

    def __init__(self, name, hp, damage, mana, race):
        self.mana = mana
        self.race = race
        super().__init__(name, hp, damage)


class Dremora(Enemy):

    def __init__(self):
        super().__init__(name="Dremora", hp=250, damage=120)


class Dragon(Enemy):

    def __init__(self):
        super().__init__(name="Dragon", hp=1000, damage=250)
