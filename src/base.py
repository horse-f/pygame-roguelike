from pygame.sprite import Sprite;

class Base(Sprite) :
    def __init__(self, image=None, rect=None):
        Sprite.__init__(self);

        self.image = image;
        self.rect = rect;

        pass;