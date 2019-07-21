from src.scenes.Scene import Scene
from src.game import SceneRouter
from src.scenes.MainScene import MainScene
from src.menus.Menu import TileMenu
from src.game import TileService
from src.menus.Menu import FancyBorder

class MenuScene(Scene):
    def start(self):
        print('started menu scene')
        self.setUpMenu()
        # SceneRouter.changeTo(MainScene())

    def end(self):
        print('im dying')

    def setUpMenu(self):
        dims = {
            'x': 8*TileService.size,
            'y': 10*TileService.size,
            'w': 10*TileService.size,
            'h': 8*TileService.size
        }
        self.menu = TileMenu(dims['x'], dims['y'], dims['w'], dims['h'], self.camera, brdr=FancyBorder())
        self.menu.addText('Hello World!', ix=0, iy=0)


