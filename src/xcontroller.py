from pygame.sprite import Group;
from pygame.sprite import Sprite;

class Controller(Group):

    # draw(surrface)
    # add(sprite)
    # remove(sprite)

    def __init__(self):
        Group.__init__(self);

        pass;

    def draw(self, display) :
        if(hasattr(self,'spritedict')):
            Group.draw(self, display);

    def sprites(self) :
        if(hasattr(self, 'spritedict')):
            return Group.sprites(self);
        else :
            return [];

        pass;

    def load(self):
        pass

    def update(self):
        pass
