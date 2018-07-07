from src.game import Engine;
from src.game import Event;
from src.game import SceneRouter;
from src.game import Keyboard;

import pygame;
from pygame.locals import *;
from pygame.time import Clock;

FRAMERATE = 144;

##############################################
def endScene(eventInfo):

    print('ending scene');

    SceneRouter.changeScene('');

    pass;
##############################################

def onQuit(eventInfo) :
    Engine.running = False;

def init():
    pygame.init();
    Engine.init();
    Engine.clock = Clock();
    pass;

def cleanup():
    pygame.quit();
    pass;

if __name__ == '__main__':
    init();

    Event.on(pygame.QUIT, onQuit);

    Engine.load();

###############################################################
    Keyboard.on(Keyboard.keymap['END_SCENE'], endScene);
###############################################################

    ##################### test ###################
    SceneRouter.changeScene('game.World');
    ##############################################

    while(Engine.running) :
        Engine.draw();
        Engine.update();
        Event.digest();
        Engine.clock.tick(FRAMERATE);

    cleanup();



    