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
    display.fill((0,0,0));

    pass;


def add(sprite):
    drawables.append(sprite);

    pass;


def remove(sprite):
    if(sprite in drawables) :
        drawables.remove(sprite);

    pass;

