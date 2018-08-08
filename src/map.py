from src.controller import Controller;
from src.game import Objects;

import pygame;

class Map(Controller):
    def __init__(self, _dir='maps/') :
        self.directory = _dir;

        pass;


    def loadMap(self, file) :
        self.layout = pygame.image.load(self.directory + file + '.png').convert();

        self.addTiles(self.layout, Objects.objectDefs['surfaces']);

        pass;


    def addTiles(self, layout, surfaces) :
        layout.lock();

        for x in range(0,layout.get_width()):
            for y in range(0,layout.get_height()) :

                pixel = layout.get_at((x,y));

                print('layout: ', pixel, x, y);

        layout.unlock();

        pass;
