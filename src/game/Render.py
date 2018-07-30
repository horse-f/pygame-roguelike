print('Render');

import pygame;

display = None;
camera = None;

def init(screenSize):
    global display;
    display = pygame.display.set_mode(screenSize, pygame.HWSURFACE | pygame.DOUBLEBUF);

    pass;

def draw() :
    camera.draw(display);

    pass;

    
def flip() :
    pygame.display.flip();

    pass;


def clear():
    display.fill((0,0,0));

    pass;

