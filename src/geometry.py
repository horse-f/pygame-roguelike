from pygame.sprite import Group;
from pygame.sprite import Sprite;

class Wall(Sprite) :
    def __init__(self):
        Sprite.__init__(self);
        self.image = None;
        self.rect = None;

class Geometry(Group):
    def __init__(self):
        Group.__init__(self);

    def load(self):
        pass

    def updateWorld(self):
        pass