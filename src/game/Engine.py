print('Engine')

import pygame
from src.game import TileService
from src.game import Config
from src.game import Render
from src.game import Keyboard
from src.game import Objects
from src.game import SceneRouter
from src.game import TurnManager

from src.scenes.MenuScene import MenuScene


scene = None;

clock = None;
running = True;
paused = False;

def init():
    Keyboard.init()
    Config.init()
    Render.init((1280,720))
    Objects.init()

def load():
    Config.load()
    Keyboard.load()
    TileService.loadTiles(Config.settings['tile_sheet'], 20)
    SceneRouter.changeTo(MenuScene())
    # load options

def update() :
    SceneRouter.update()

def draw() :
    Render.clear()
    Render.draw()
    Render.flip()

