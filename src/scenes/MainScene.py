from src.scenes.Scene import Scene
from src.gameobjects.Character import Character
from src.gameobjects.NPC import NPC
from src.game import TileService
from pygame.color import Color
from src.scripts import *
from src.game import TurnManager

class MainScene(Scene):
    def start(self):
        print('starting main scene')
        self.character = Character((0,4), camera=self.camera)
        self.npc = NPC((12,6), self.camera, 4*TileService.size, 3*TileService.size, color=Color('green'))
        self.npc.attachScript(lizard_wizard.ai())
        self.shop_keeper = NPC((13,4), self.camera, 10*TileService.size, 9*TileService.size, color=Color('red'))
        self.shop_keeper.attachScript(dev_shop_keeper.ai())

    def end(self):
        print('save??')

    def update(self):
        # mode?
        TurnManager.update()
        if(TurnManager.peekTurn() > 0):
            self.npc.update()
            self.shop_keeper.update()
            TurnManager.clear()