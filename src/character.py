print('character');

import pygame;
from src.game import Engine;
from src.game import Render;
from src.game import TileService;
from src.base import Base;
from src.game import Keyboard;

class Character(Base) :
    def __init__(self) :
        self.pos = (0,0);
        self.tile = None;

        # collisions


class CharacterController(Base) : 
    def __init__(self) :
        self.Character = Character();

        # read controls from file
        Keyboard.on([{
            'key': pygame.K_UP,
            'mod': pygame.KMOD_NONE
        }, {
            'key': pygame.K_KP8,
            'mod': pygame.KMOD_NONE
        }], self.moveUp);

        Keyboard.on([{
            'key': pygame.K_DOWN,
            'mod': pygame.KMOD_NONE
        }, {
            'key': pygame.K_KP2,
            'mod': pygame.KMOD_NONE
        }], self.moveDown);

        Keyboard.on([{
            'key': pygame.K_RIGHT,
            'mod': pygame.KMOD_NONE
        }, {
            'key': pygame.K_KP6,
            'mod': pygame.KMOD_NONE
        }], self.moveRight);

        Keyboard.on([{
            'key': pygame.K_LEFT,
            'mod': pygame.KMOD_NONE
        }, {
            'key': pygame.K_KP4,
            'mod': pygame.KMOD_NONE
        }], self.moveLeft);

        Keyboard.on([{
            'key': pygame.K_KP9,
            'mod': pygame.KMOD_NONE
        }], self.moveUpRight);

        Keyboard.on([{
            'key': pygame.K_KP7,
            'mod': pygame.KMOD_NONE
        }], self.moveUpLeft);

        Keyboard.on([{
            'key': pygame.K_KP3,
            'mod': pygame.KMOD_NONE
        }], self.moveDownRight);

        Keyboard.on([{
            'key': pygame.K_KP1,
            'mod': pygame.KMOD_NONE
        }], self.moveDownLeft);


    def load(self) :
        self.Character.tile = TileService.getTile('blah');

    def update(self) :
        pass;

    def draw(self) : 
        Render.draw(self.Character.tile, self.Character.pos);

    ## character actions

    def moveUp(self, eventInfo):
        print('moving up', eventInfo);

    def moveDown(self, eventInfo):
        print('moving down', eventInfo);

    def moveRight(self, eventInfo):
        print('moving right', eventInfo);

    def moveLeft(self, eventInfo):
        print('moving left', eventInfo);

    def moveUpRight(self, eventInfo):
        print('moving up and right', eventInfo);

    def moveUpLeft(self, eventInfo):
        print('moving up and left', eventInfo);

    def moveDownRight(self, eventInfo):
        print('moving down and right', eventInfo);

    def moveDownLeft(self, eventInfo):
        print('moving down and left', eventInfo);

    # other things like control setup

# register controller
Engine.controller(CharacterController());
