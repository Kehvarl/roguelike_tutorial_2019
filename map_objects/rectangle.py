from random import randint

class Rect:
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.width = w
        self.height = h
        self.x2 = x + w
        self.y2 = y + h

    def center(self):
        center_x = int(self.x1 + (self.width // 2))
        center_y = int(self.y1 + (self.height // 2))
        return (center_x, center_y)

    def random_point(self):
        x = randint(self.x1 + 1, self.x2 - 1)
        y = randint(self.y1 + 1, self.y2 - 1)
        return x,y

    def intersect(self, other):
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and
                self.y1 <= other.y2 and self.y2 >= other.y1)

