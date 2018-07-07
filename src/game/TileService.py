print('tile service');

import pygame;

tiles = None;
size = 0;

def getTile(pos):
    surf = pygame.Surface((size,size));
    rect = (pos[0]*size, pos[1]*size, size, size);
    surf.blit(tiles, (0,0), rect);

    return surf;

def loadTiles(src, s) :
    global tiles;
    global size;
    size = s;
    tiles = pygame.image.load(src).convert();

    pass;