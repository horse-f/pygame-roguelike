from src.controller import Controller;
from src.game import Objects;
from src.game import TileService;
from src.base import Base;

import pygame;

def getDef(pixel):
    surfaces = Objects.objects['surfaces'];

    for surf in surfaces:
        colorKey = surf['colorKey'];
        if( pixel.r == colorKey[0] and pixel.g == colorKey[1] and pixel.b == colorKey[2]) :
            return surf;

    return None;

def getTile(tiles) :
    # todo: logic to pick a tile based on random or sequential

    tile = tiles[0];

    return TileService.getTile((tile['sprite'][0], tile['sprite'][1]));


class MapSurface(Base) :
    def __init__(self, tile=None, size=0, worldPosition={'x':0,'y':0}, collisions=False):
        Base.__init__(self,tile, size, worldPosition);

        pass;


class Map(Controller):
    def __init__(self, _dir='maps/') :
        Controller.__init__(self);

        self.directory = _dir;

        pass;


    def loadMap(self, file) :
        self.layout = pygame.image.load(self.directory + file + '.png').convert();

        self.addTiles(self.layout);

        pass;


    def addTiles(self, layout) :
        layout.lock();

        size = TileService.size;

        for x in range(0,layout.get_width()):
            for y in range(0,layout.get_height()) :

                pixel = layout.get_at((x,y));

                _def = getDef(pixel);

                if(_def is not None) :
                    tile = getTile(_def['tiles']);

                    mapSurface = MapSurface(tile, worldPosition={'x':x*size,'y':y*size}, collisions=_def['collisions']);
                    mapSurface.size = TileService.size;

                    self.add(mapSurface);


        layout.unlock();

        pass;


