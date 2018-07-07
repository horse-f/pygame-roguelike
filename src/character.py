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
        pass;

    def move(self,x,y) :
        # check collisions
        self.rect = (
            self.rect[0] + x * TileService.size,
            self.rect[1] + y * TileService.size,
            TileService.size,
            TileService.size
        );
        pass;


class CharacterController(Controller) :
    def __init__(self, _character) :
        self.character = _character;
        pass;

    def load(self) :
        self.character.image = TileService.getTile((0,4));
        self.character.rect  = (
            1 * TileService.size,
            4 * TileService.size,
            TileService.size,
            TileService.size
        );

        Keyboard.on(Keyboard.keymap['MOVE_UP'], self.moveUp);
        Keyboard.on(Keyboard.keymap['MOVE_RIGHT'], self.moveRight);
        Keyboard.on(Keyboard.keymap['MOVE_LEFT'], self.moveLeft);
        Keyboard.on(Keyboard.keymap['MOVE_DOWN'], self.moveDown);
        Keyboard.on(Keyboard.keymap['MOVE_UP_RIGHT'], self.moveUpRight);
        Keyboard.on(Keyboard.keymap['MOVE_UP_LEFT'], self.moveUpLeft);
        Keyboard.on(Keyboard.keymap['MOVE_DOWN_RIGHT'], self.moveDownRight);
        Keyboard.on(Keyboard.keymap['MOVE_DOWN_LEFT'], self.moveDownLeft);
        pass;


    def update(self) :
        pass;



    ## character actions

    def moveUp(self, eventInfo):
        self.character.move(0,-1);
        pass;

    def moveDown(self, eventInfo):
        self.character.move(0, 1);
        pass;

    def moveRight(self, eventInfo):
        self.character.move(1,0);
        pass;

    def moveLeft(self, eventInfo):
        self.character.move(-1,0);
        pass;

    def moveUpRight(self, eventInfo):
        self.character.move(1,-1);
        pass;

    def moveUpLeft(self, eventInfo):
        self.character.move(-1,-1);
        pass;

    def moveDownRight(self, eventInfo):
        self.character.move(1,1);
        pass;

    def moveDownLeft(self, eventInfo):
        self.character.move(-1,1);
        pass;

    # other things like control setup

