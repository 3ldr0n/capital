class Enemy:

    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage


class Draugr(Enemy):

    def __init__(self):
        super().__init__(name="Draugr", hp=100, damage=20)


class Dragon(Enemy):

    def __init__(self):
        super().__init__(name="Dragon", hp=1000, damage=190)


