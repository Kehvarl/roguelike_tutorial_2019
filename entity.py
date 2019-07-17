class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """
    def __init__(self, x, y, char, color, name, blocks=False, combat=None, ai=None):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks = blocks
        self.combat = combat
        self.ai = ai

        if self.combat:
            self.combat.owner = self

        if self.ai:
            self.ai.owner = self

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


def get_blocking_entities_at_location(entities, destination_x, destination_y):
    for entity in entities:
        if entity.blocks and entity.x == destination_x and entity.y == destination_y:
            return entity
    return None

