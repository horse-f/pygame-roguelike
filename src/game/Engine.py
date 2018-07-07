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
    Render.init((1280,720));
    Keyboard.init();
    Config.init();

def load() :
    Config.load();
    Keyboard.load();
    TileService.loadTiles(Config.settings['tile_sheet'], 20);
    SceneRouter.load();

def update() :
    SceneRouter.update();

# def updateWorld() :
#     SceneRouter.updateWorld();

def draw() :
    Render.clear();
    Render.draw();
    Render.flip();

