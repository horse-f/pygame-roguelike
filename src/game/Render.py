print('Render');

import pygame;
from src.game import SceneRouter

display = None;

def init(screenSize):
    global display;
    display = pygame.display.set_mode(screenSize, pygame.HWSURFACE | pygame.DOUBLEBUF);

def draw() :
    camera = SceneRouter.scene.camera
    if(camera is not None):
        camera.draw(display);
    
def flip() :
    pygame.display.flip();

def clear():
#     display.fill((0,0,0));
    camera = SceneRouter.scene.camera       
    if(camera is not None):
        camera.clear(display,clearCallback)

def clearCallback(surf, rect):
    surf.fill((0,0,0), rect)
