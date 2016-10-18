#!/opt/local/Library/Frameworks/Python.framework/Versions/2.7/bin/python

# package to contain all enemies

class Enemy(object):
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

# don't need to include is_alive method in the
# sub class because they get access to the methods
# in the superclass

class GiantSpider(Enemy):
    def __init__(self):
        super(GiantSpider, self).__init__(name="Giant Spider",
                                            hp=10,
                                        damage=2)

class Ogre(Enemy):
    def __init__(self):
        super(Ogre, self).__init__(name="Ogre",
                                     hp=30,
                                 damage=15)
