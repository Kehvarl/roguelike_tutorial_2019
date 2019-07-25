import math
import tcod as libtcod

from render_functions import RenderOrder


class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """
    def __init__(self, x, y, char, color, name, blocks=False, render_order=RenderOrder.CORPSE, combat=None, ai=None):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.label = None
        self.blocks = blocks
        self.render_order = render_order
        self.combat = combat
        self.ai = ai
        self.fade = False

        if self.combat:
            self.combat.owner = self

        if self.ai:
            self.ai.owner = self

    def set_ai(self, ai):
        self.ai = ai
        self.ai.owner = self

    def title(self):
        if self.label is None:
            return self.name
        else:
            return '{} of {}'.format(self.label, self.name)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_towards(self, target_x, target_y, game_map, entities):
        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        dx = int(round(dx / distance))
        dy = int(round(dy / distance))

        new_x = self.x + dx
        new_y = self.y + dy

        if not (game_map.is_blocked(new_x, new_y) or 
                get_blocking_entities_at_location(entities, new_x, new_y)):
            self.move(dx, dy)

    def move_astar(self, target, entities, game_map):
        fov = game_map.new_fov_map()

        for entity in entities:
            if entity.blocks and entity != self and entity != target:
                libtcod.map_set_properties(fov, entity.x, entity.y, True, False)

        my_path = libtcod.path_new_using_map(fov, 1.41)

        libtcod.path_compute(my_path, self.x, self.y, target.x, target.y)

        if not libtcod.path_is_empty(my_path) and libtcod.path_size(my_path) < 25:
            x, y = libtcod.path_walk(my_path, True)
            if x or y:
                self.x = x
                self.y = y

        else:
            self.move_towards(target.x, target.y, game_map, entities)
        
        libtcod.path_delete(my_path)

    def distance_to(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)


def get_blocking_entities_at_location(entities, destination_x, destination_y):
    for entity in entities:
        if entity.blocks and entity.x == destination_x and entity.y == destination_y:
            return entity
    return None
