print('character');

import pygame;

from src.game import Keyboard;
from src.game import TileService;
# from src.game import Collisions;

from src.base import Base;
from src.controller import Controller;


CHARACTER_INPUT_GROUP = 'CHARACTER';

class Character(Base) :
    def __init__(self,image=None,size=0,pos={'x':0,'y':0}) :
        Base.__init__(self,image,size,pos);

        # collisions
        pass;

    def move(self,x,y) :
        self.pos['x'] += x * self.size;
        self.pos['y'] += y * self.size;

        pass;


class CharacterController(Controller) :
    def __init__(self, _character, inputGroupName=None) :
        Controller.__init__(self);

        self.character = _character;
        self.inputGroup = inputGroupName if inputGroupName is not None else CHARACTER_INPUT_GROUP;

        self.add(self.character);

        pass;

    def load(self) :
        self.character.size  = TileService.size;
        self.character.image = TileService.getTile((0,4));

        ###################################################
        self.character.setPos({
            'x': 1 * TileService.size,
            'y': 4 * TileService.size
        });
        ###################################################

        Keyboard.on(Keyboard.keymap['MOVE_UP'], self.moveUp, self.inputGroup);
        Keyboard.on(Keyboard.keymap['MOVE_RIGHT'], self.moveRight, self.inputGroup);
        Keyboard.on(Keyboard.keymap['MOVE_LEFT'], self.moveLeft, self.inputGroup);
        Keyboard.on(Keyboard.keymap['MOVE_DOWN'], self.moveDown, self.inputGroup);
        Keyboard.on(Keyboard.keymap['MOVE_UP_RIGHT'], self.moveUpRight, self.inputGroup);
        Keyboard.on(Keyboard.keymap['MOVE_UP_LEFT'], self.moveUpLeft, self.inputGroup);
        Keyboard.on(Keyboard.keymap['MOVE_DOWN_RIGHT'], self.moveDownRight, self.inputGroup);
        Keyboard.on(Keyboard.keymap['MOVE_DOWN_LEFT'], self.moveDownLeft, self.inputGroup);
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

