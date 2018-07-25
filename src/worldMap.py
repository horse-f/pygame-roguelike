from src.base import Base;
from src.controller import Controller;

from src.game import TileService;

class Wall(Base) :
    def __init__(self, image=None, size=0, pos=None):
        Base.__init__(self, image,size,pos);
        pass;

class Floor(Base) :
    def __init__(self, image=None,size=0,pos=None):
        Base.__init__(self, image,size,pos);
        pass;


class WorldMap(Controller):
    def __init__(self):
        Controller.__init__(self);
        pass;


    def load(self):
        pass;


    def update(self):
        pass;


    def buildMap(self):

        print('building stuff');
##################################################

        image = TileService.getTile((9,0));
        size  = TileService.size;
        pos   = {
            'x': 10 * size,
            'y': 10 * size
        };
        # rect  = tuple([ TileService.size * i for i in (10, 10, 1, 1)]);

        wall = Wall(image,size,pos);
        # wall.rect = rect;

        self.add(wall);


        pass;

##################################################
