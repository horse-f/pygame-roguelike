from src.game import Engine;
from src.game import Event;
from src.game import SceneRouter;

import pygame;
from pygame.locals import *;
from pygame.time import Clock;

FRAMERATE = 144;

def onQuit(eventInfo) :
    Engine.running = False;

def init():
    pygame.init();
    Engine.init();
    Engine.clock = Clock();

def cleanup():
    pygame.quit();

if __name__ == '__main__':
    init();

    Event.on(pygame.QUIT, onQuit);

    Engine.load();

    ##################### test ###################
    SceneRouter.changeScene('game.World');
    ##############################################

    while(Engine.running) :
        # Event.digest();
        Engine.draw();
        Engine.update();
        Engine.clock.tick(FRAMERATE);

    cleanup();



    