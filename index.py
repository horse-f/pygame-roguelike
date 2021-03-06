from src.game import Engine;
from src.game import Event;
from src.game import SceneRouter;
from src.game import Keyboard;
from src.game import Render;

import pygame;
from pygame.locals import *;
from pygame.time import Clock;
import pygame.time;

FRAMERATE = 144;

drawTime   = 0;
updateTime = 0;
eventTime  = 0;

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

    while(Engine.running) :

        drawTime = pygame.time.get_ticks();
        Engine.draw();
        drawTime = pygame.time.get_ticks() - drawTime;
        # print('draw', drawTime);

        updateTime = pygame.time.get_ticks();
        Engine.update();
        updateTime = pygame.time.get_ticks() - updateTime;
        # print('update', updateTime);

        eventTime = pygame.time.get_ticks();
        Event.digest();
        eventTime = pygame.time.get_ticks() - eventTime;
        # print('event', eventTime);

        Engine.clock.tick(FRAMERATE);

        # print('FPS', Engine.clock.get_fps());s
        # print('frame', Engine.clock.get_time());

    cleanup();



    