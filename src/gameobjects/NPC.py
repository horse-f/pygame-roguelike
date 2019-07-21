from src.gameobjects.GameObject import GameObject
from src.game import TileService
from pygame.sprite import Sprite
from pygame.color import Color

class NPC(GameObject):
    def __init__(self, tile, camera, wx=0, wy=0, color=Color(255,255,255)):
        self.size = TileService.size
        GameObject.__init__(self, self.size, self.size, wx, wy)
        sprite = Sprite()
        sprite.image = TileService.getTile(tile, color)
        sprite.rect = (
            wx,
            wy,
            self.size,
            self.size
        )
        self.addSprites(sprite, camera)
