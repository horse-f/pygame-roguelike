from pygame.sprite import Sprite;
from copy import copy;

class Base(Sprite) :
    def __init__(self, image=None, size=0, pos={'x':0,'y':0}):
        Sprite.__init__(self);

        self.image = image;
        self.size = size;

        self.setPos(pos);

        pass;

    def setPos(self, pos):
        self.pos = copy(pos);
        self.rect = (
            self.pos['x'],
            self.pos['y'],
            self.size,
            self.size
        );

        pass;