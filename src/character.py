print('character');

import pygame;
from src.game import Engine;
from src.game import Render;
from src.game import TileService;
from src.base import Base;
from src.game import Keyboard;

class Character(Base) :
    def __init__(self) :
        self.pos = {
            'x': 20,
            'y': 80
        };
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
        self.Character.tile = TileService.getTile((0,4));

    # def update(self) :
    #     pass;

    # def updateWorld(self):
    #     pass

    def draw(self) : 
        Render.draw(self.Character.tile, self.Character.pos);

    ## character actions

    def moveUp(self, eventInfo):
        self.Character.pos['y'] += -self.Character.tile.size['h'];
        # print('********* moving up', self.Character.pos);

    def moveDown(self, eventInfo):
        self.Character.pos['y'] += self.Character.tile.size['h'];
        # print('********* moving down', self.Character.pos);

    def moveRight(self, eventInfo):
        self.Character.pos['x'] += self.Character.tile.size['w'];
        # print('********* moving right', self.Character.pos);

    def moveLeft(self, eventInfo):
        self.Character.pos['x'] += -self.Character.tile.size['w'];
        # print('********* moving left', self.Character.pos);

    def moveUpRight(self, eventInfo):
        self.Character.pos['x'] += self.Character.tile.size['w'];
        self.Character.pos['y'] += -self.Character.tile.size['h'];
        # print('********* moving up and right', self.Character.pos);

    def moveUpLeft(self, eventInfo):
        self.Character.pos['x'] += -self.Character.tile.size['w'];
        self.Character.pos['y'] += -self.Character.tile.size['h'];
        # print('********* moving up and left', self.Character.pos);

    def moveDownRight(self, eventInfo):
        self.Character.pos['x'] += self.Character.tile.size['w'];
        self.Character.pos['y'] += self.Character.tile.size['h'];
        # print('********* moving down and right', self.Character.pos);

    def moveDownLeft(self, eventInfo):
        self.Character.pos['x'] += -self.Character.tile.size['w'];
        self.Character.pos['y'] += self.Character.tile.size['h'];
        # print('********* moving down and left', self.Character.pos);

    # other things like control setup

# register controller
Engine.controller(CharacterController());
