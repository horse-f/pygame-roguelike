print('Render');

import pygame;
from pygame.sprite import RenderClear;

display = None;
renderGroup = RenderClear();


def init(screenSize):
    global display;
    display = pygame.display.set_mode(screenSize, pygame.HWSURFACE | pygame.DOUBLEBUF);
    pass;

def draw() :
    renderGroup.draw(display);
    pass;

    
def flip() :
    pygame.display.flip();
    pass;


def clear():
    def cb(surf, rect) :
        surf.fill((0,0,0),rect);

    renderGroup.clear(display, cb);
    pass;


def add(sprite):
    renderGroup.add(sprite);
    pass;


def remove(sprite):
    renderGroup.remove(sprite);
    pass;

