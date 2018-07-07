print('character');

import pygame;
from src.game import TileService;
from src.controller import Controller;
from src.game import Keyboard;
from pygame.sprite import Sprite;

class Character(Sprite) :
    def __init__(self) :
        Sprite.__init__(self);
        self.image = None;
        self.rect = None;

        # collisions

    def move(self,x,y) :
        # check collisions
        self.rect = (
            self.rect[0] + x * TileService.size,
            self.rect[1] + y * TileService.size,
            TileService.size,
            TileService.size
        );


class CharacterController(Controller) : 
    def __init__(self, _character) :
        self.character = _character;


    def load(self) :
        self.character.image = TileService.getTile((0,4));
        self.character.rect  = (
            1 * TileService.size,
            4 * TileService.size,
            TileService.size,
            TileService.size
        );

    def update(self) :
        Keyboard.ifAction(Keyboard.keymap['MOVE_UP'], moveUp);
        pass;

    # def updateWorld(self):

    ## character actions

    def moveUp(self, eventInfo):
        self.character.move(0,-1);

    def moveDown(self, eventInfo):
        self.character.move(0, 1);

    def moveRight(self, eventInfo):
        self.character.move(1,0);

    def moveLeft(self, eventInfo):
        self.character.move(-1,0);

    def moveUpRight(self, eventInfo):
        self.character.move(1,-1);

    def moveUpLeft(self, eventInfo):
        self.character.move(-1,-1);

    def moveDownRight(self, eventInfo):
        self.character.move(1,1);

    def moveDownLeft(self, eventInfo):
        self.character.move(-1,1);

    # other things like control setup

