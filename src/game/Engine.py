print('Engine');

import pygame;
from src.game import TileService;

controllers = [];

clock = None;
running = True;
paused = True;

def load() : 
    TileService.loadTiles('src', 20);

    for _controller in controllers :
        _controller.load();

def update() :
    for _controller in controllers :
        _controller.update();

def updateWorld() :
    for _controller in controllers : 
        _controller.updateWorld();

def draw() :
    for _controller in controllers : 
        _controller.draw();


def controller(ctl) :
    controllers.append(ctl);
