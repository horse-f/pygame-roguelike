print('Render');

import pygame;
from pygame.sprite import RenderClear;

display = None;
renderGroup = RenderClear();


def init(screenSize):
    global display;
    display = pygame.display.set_mode(screenSize, pygame.HWSURFACE | pygame.DOUBLEBUF);

def draw() :
    renderGroup.draw(display);
    
def flip() :
    pygame.display.flip();

def clear():
    def cb(surf, rect) :
        surf.fill((0,0,0),rect);

    renderGroup.clear(display, cb);

def add(sprite):
    renderGroup.add(sprite);

def remove(sprite):
    renderGroup.remove(sprite);
