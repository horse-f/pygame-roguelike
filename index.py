from src.game import Engine;
from src.game import Render;
from src.game import Keyboard;
from src.game import Event;

import pygame;
from pygame.locals import *;
from pygame.time import Clock;

FRAMERATE = 60;

def onQuit(eventInfo) :
    print('handling event', eventInfo);
    Engine.running = False;
    cleanup();

def init():
    pygame.init();
    Render.init((1280,720));
    Keyboard.init();
    Engine.clock = Clock();

def cleanup():
    pygame.quit();

if __name__ == '__main__':
    init();

    Event.on(pygame.QUIT, onQuit);

    # Keyboard.on([{
    #     'key': pygame.K_c,
    #     'mod': pygame.KMOD_LCTRL
    # }, {
    #     'key': pygame.K_c,
    #     'mod': pygame.KMOD_RCTRL
    # }], onQuit);

    Engine.load();

    while(Engine.running) :
        Event.digest();

        Engine.draw();
        Engine.update();

        if(not Engine.paused) :
            Engine.updateWorld();

        Engine.clock.tick(FRAMERATE);

    cleanup();



    