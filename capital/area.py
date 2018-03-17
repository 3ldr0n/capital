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

class Area:

    def __init__(self, name, description="Empty room", possible_directions={}):
        self.name = name
        self.description = description
        self.possible_directions = possible_directions


    def neighbor(self, direction):
        if direction in self.possible_directions:
            return self.possible_directions[direction]

        return None


    def go_north(self):
        return self.neighbor('north')


    def go_south(self):
        return self.neighbor('south')


    def go_west(self):
        return self.neighbor('west')


    def go_east(self):
        return self.neighbor('east')
