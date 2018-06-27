print('character');

import pygame;
from src.game import Engine;
from src.game import Render;
from src.game import TileService;
from src.base import Base;
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
        self.Character.image = TileService.getTile((0,4));
        self.Character.rect  = (
            1 * TileService.size,
            4 * TileService.size,
            TileService.size,
            TileService.size
        );
        Render.add(self.Character);

    # def update(self) :
    #     pass;

    # def updateWorld(self):
    #     pass

    ############## dont need this
    # def draw(self) : 
    #     Render.draw(self.Character.tile, self.Character.pos);

    ## character actions

    def moveUp(self, eventInfo):
        self.Character.move(0,-1);

    def moveDown(self, eventInfo):
        self.Character.move(0, 1);

    def moveRight(self, eventInfo):
        self.Character.move(1,0);

    def moveLeft(self, eventInfo):
        self.Character.move(-1,0);

    def moveUpRight(self, eventInfo):
        self.Character.move(1,-1);

    def moveUpLeft(self, eventInfo):
        self.Character.move(-1,-1);

    def moveDownRight(self, eventInfo):
        self.Character.move(1,1);

    def moveDownLeft(self, eventInfo):
        self.Character.move(-1,1);

    # other things like control setup

# register controller
Engine.controller(CharacterController());
