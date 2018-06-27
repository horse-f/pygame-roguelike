print('Engine');

import pygame;
from src.game import TileService;
from src.game import Config;
from src.game import Render;

controllers = [];

clock = None;
running = True;
paused = True;

def load() : 
    TileService.loadTiles(Config.settings['tileSheet'], 20);

    for _controller in controllers :
        _controller.load();

def update() :
    for _controller in controllers :
        _controller.update();

def updateWorld() :
    for _controller in controllers : 
        _controller.updateWorld();

def draw() :
    Render.clear();
    Render.draw();
    Render.flip();

    # for _controller in controllers : 
    #     _controller.draw();


def controller(ctl) :
    controllers.append(ctl);
