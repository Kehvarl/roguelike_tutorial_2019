from map_objects.tile import Tile


class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        tiles = [[Tile(True) for _ in range(self.height)] for _ in range(self.width)]

        return tiles

    def is_blocked(self, x, y):
        return self.tiles[x][y].blocked
