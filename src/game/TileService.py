print('tile service');

import pygame;
from pygame.color import Color

tiles = None;
size = 0;
background = Color(0,0,0)

def changeColor(surf, color, bgnd):
    surf.lock()
    for x in range(0,surf.get_width()):
        for y in range(0,surf.get_height()):
            pixel = surf.get_at((x, y))
            if(pixel != bgnd):
                surf.set_at((x, y), color)
    surf.unlock()
    return surf

def getTileByChar(char, color=Color(255,255,255)):
    o = ord(char)
    x = o & 0x0f
    y = o >> 4
    return getTile((x,y), color)

def getTile(pos, color=Color(255,255,255)):
    global background
    surf = pygame.Surface((size,size));
    rect = (pos[0]*size, pos[1]*size, size, size);
    surf.blit(tiles, (0,0), rect);
    surf = changeColor(surf, color, background)
    return surf;

def loadTiles(src, s, bg=Color(0,0,0)) :
    global tiles;
    global size;
    global background
    size = s;
    tiles = pygame.image.load(src).convert();
    background = bg
