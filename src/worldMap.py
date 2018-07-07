from src.base import Base;
from src.controller import Controller;

from src.game import TileService;

class Wall(Base) :
    def __init__(self, image=None, rect=None):

        print('image', image);
        print('rect', rect);

        Base.__init__(self, image, rect);
        pass;

class Floor(Base) :
    def __init__(self, image=None, rect=None):
        Base.__init__(self, image, rect);
        pass;


class WorldMap(Controller):
    def __init__(self):
        Controller.__init__(self);
        self.test  = None;

        
        pass;


    def load(self):
        pass;


    def update(self):
        pass;


    def buildMap(self):

        ############## TEST ###############

        image = TileService.getTile((9,0));
        rect = tuple([ TileService.size * i for i in (10, 10, 1, 1)]);

        self.test = Wall(image,rect);

        self.add(self.test);

        print('test', self.test);


        ###################################

        pass;