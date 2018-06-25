print('tile service');

from src.game.sprite import Sprite;
from src.game import SpriteService;

# get tile sheet
tiles = None;
size = 0;

def getTile(tileName):
    return Sprite(None, (size, size));

def loadTiles(src, s) :
    size = s;
    tiles = SpriteService.loadSpriteSheet(src, (size, size));