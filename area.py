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
