#!/opt/local/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import items, enemies

# Master Class: MapTile. Will build upon this with subclasses

class MapTile(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

class StartingRoom(MapTile):
    def intro_text(self):
        return"""
        You find yourself in a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """

    def modify_player(self, player):
        #Room has no action on player.
        pass

class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super(LootRoom, self).__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)

class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super(EnemyRoom, self).__init__(x, y)

    def modify_player(self, player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining".format(self.enemy.damage, the_player.hp))

class EmptyCavePath(MapTile):
    def intro_text(self):
        return """
        Another unremarkable part of the cave. You must forge onwards.
        """

    def modify_player(self, player):
        #room has no effect on play
        pass

class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super(GiantSpiderRoom, self).__init__(self, x, y, enemies.GiantSpider())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A giant spider jumps down from its web in front of you!
            """
        else:
            return """
            The corpse of a dead spider rots on the ground.
            """

class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super(FindDaggerRoom, self).__init__(self, x, y, items.Dagger())

    def intro_text(self):
        return """
        Your notice something shiny in the corner.
        It's a dagger! You pick it up.
        """
