print('Render');

import pygame;

display = None;

def init(screenSize):
    global display;
    display = pygame.display.set_mode(screenSize, pygame.HWSURFACE | pygame.DOUBLEBUF);

def draw(sprite, pos) :
    if(sprite.surf) :
        # print('drawing', sprite, 'at', (pos['x'], pos['y']));
        display.blit(sprite.surf,(pos['x'], pos['y']));
    
def flip() :
    pygame.display.flip();

def clear():
    display.fill((0,0,0));
