import tcod as libtcod
from random import randint
from entity import Entity
from components.combat import Combat
from components.item import Item
from components.ai import BasicMonster
from map_objects.rectangle import Rect
from map_objects.tile import Tile
from render_functions import RenderOrder

class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        tiles = [[Tile(True) for _ in range(self.height)] for _ in range(self.width)]

        return tiles

    def make_map(self, max_rooms, room_min_size, room_max_size, player, entities, max_monsters_per_room, max_items_per_room):
        rooms = []
        num_rooms = 0
        
        for r in range(max_rooms):
            w = randint(room_min_size, room_max_size)
            h = randint(room_min_size, room_max_size)
            x = randint(0, self.width - w - 1)
            y = randint(0, self.height - h - 1)

            new_room = Rect(x, y, w, h)

            for other_room in rooms:
                if new_room.intersect(other_room):
                    break
            else:
                self.create_room(new_room)
                (new_x, new_y) = new_room.center()

                if num_rooms ==0:
                    player.x = new_x
                    player.y = new_y
                else:
                    (prev_x, prev_y) = rooms[num_rooms -1].center()
                    if(randint(0, 1) == 1):
                        self.create_h_tunnel(prev_x, new_x, prev_y)
                        self.create_v_tunnel(prev_y, new_y, new_x)
                    else:
                        self.create_v_tunnel(prev_y, new_y, prev_x)
                        self.create_h_tunnel(prev_x, new_x, new_y)

                self.place_monsters(new_room, entities, max_monsters_per_room)
                self.place_items(new_room, entities, max_items_per_room)

                rooms.append(new_room)
                num_rooms += 1

    def create_room(self, room):
       for x in range(room.x1 + 1, room.x2):
           for y in range(room.y1 + 1, room.y2):
               self.tiles[x][y].blocked = False
               self.tiles[x][y].block_sight = False

    def create_h_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    def create_v_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    def place_monsters(self, room, entities, max_monsters_per_room):
        number_of_monsters = randint(0, max_monsters_per_room)

        for i in range(number_of_monsters):
            x,y = room.random_point()

            if not any([entity for entity in entities if entity.x == x and entity.y == y]):
                if randint(0, 100) < 80:
                    combat_component = Combat(hp=10, defense=0, power=3)
                    ai_component = BasicMonster()

                    monster = Entity(x, y, 'o', libtcod.desaturated_green, 'Orc', blocks=True, render_order = RenderOrder.ACTOR, combat=combat_component, ai=ai_component)
                else:
                    combat_component = Combat(hp=16, defense=1, power=4)
                    ai_component = BasicMonster()
                    monster = Entity(x, y, 'T', libtcod.darker_green, 'Troll', blocks=True, render_order = RenderOrder.ACTOR, combat=combat_component, ai=ai_component)

                entities.append(monster)

    def place_items(self, room, entities, max_items_per_room):
        number_of_items = randint(0, max_items_per_room)

        for i in range(number_of_items):
            x,y = room.random_point()

            if not any([entity for entity in entities if entity.x == x and entity.y == y]):
                item_component = Item()
                item = Entity(x, y, '!', libtcod.violet, 'Healing Potion', render_order=RenderOrder.ITEM, item=item_component)

                entities.append(item)

    def is_blocked(self, x, y):
        return self.tiles[x][y].blocked


    def new_fov_map(self):
        fov = libtcod.map_new(self.width, self.height)

        for y1 in range(self.height):
            for x1 in range(self.width):
                libtcod.map_set_properties(fov, x1, y1, not self.tiles[x1][y1].block_sight, not self.tiles[x1][y1].blocked)
    
        return fov
   
