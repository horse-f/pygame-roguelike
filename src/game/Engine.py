print('Engine');

import pygame;
from src.game import TileService;
from src.game import Config;
from src.game import Render;
from src.game import SceneRouter;
from src.game import Keyboard;

scene = None;

clock = None;
running = True;
paused = False;

def init():
    Keyboard.init();
    Config.init();
    Render.init((1280,720));
    pass;

def load() :
    Config.load();
    Keyboard.load();
    TileService.loadTiles(Config.settings['tile_sheet'], 20);
    SceneRouter.load();
    pass;

def update() :
    SceneRouter.update();
    pass;

def draw() :
    Render.clear();
    Render.draw();
    Render.flip();
    pass;

