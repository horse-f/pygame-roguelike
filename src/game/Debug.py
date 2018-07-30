print('Debug');

from src.game import Render;
from src.game import Debug;

from pygame import font;
from pygame import Surface;
import pygame;

debugFont = None;
color = (255,255,255);

debugSurf = None;
buffSurf  = None;

hasBuff = False;
drawn = False;

transparentColor = (255,0,255);

def init():
    global debugFont;
    global debugSurf;
    global buffSurf;

    debugFont = font.SysFont('Arial', 16);

    debugSurf = Surface((Render.display.get_width(), Render.display.get_height()), pygame.HWSURFACE);
    debugSurf.fill(transparentColor);
    debugSurf.set_colorkey(transparentColor);

    buffSurf = debugSurf.copy();

    pass;


def drawString(_string, pos):
    global hasBuff;

    textSurf = debugFont.render(_string, False, color, transparentColor);

    if(drawn) :
        buffSurf.blit(textSurf,pos);
        hasBuff = True;
    else :
        debugSurf.blit(textSurf, pos);


    pass;

def draw(display):
    global drawn;
    global hasBuff;

    if(hasBuff) :
        debugSurf.blit(buffSurf, (0,0));
        buffSurf.fill(transparentColor);
        hasBuff = False;

    display.blit(debugSurf,(0,0));

    drawn = True;

    pass;

def clear():
    global drawn;

    debugSurf.fill(transparentColor);
    drawn = False;

    pass;


