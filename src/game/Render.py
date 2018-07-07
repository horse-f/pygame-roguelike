print('Render');

import pygame;

display = None;
drawables = [];

def init(screenSize):
    global display;
    display = pygame.display.set_mode(screenSize, pygame.HWSURFACE | pygame.DOUBLEBUF);

    pass;

def draw() :
    for drawable in drawables :
        drawable.draw(display);

    pass;

    
def flip() :
    pygame.display.flip();

    pass;


def clear():
    def cb(surf, rect) :
        surf.fill((0,0,0),rect);

    for drawable in drawables :
        drawable.clear(display, cb);

    pass;


def add(sprite):
    drawables.append(sprite);

    pass;


def remove(sprite):
    drawables.remove(sprite);

    pass;

