from pygame.sprite import Sprite
from pygame.color import Color
from src.gameobjects.GameObject import GameObject
from src.game import SceneRouter
from src.game import TileService
from src.game import Keyboard
from src.game import TurnManager
from functools import partial

CHARACTER_INPUT_GROUP = 'PLAYER_CHARACTER';

class Character(GameObject):
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
        Keyboard.on(Keyboard.keymap['TICK'], self.passTurn, CHARACTER_INPUT_GROUP)
        Keyboard.on(Keyboard.keymap['MOVE_UP'], partial(self.moveCharacter,0,-1*self.size), CHARACTER_INPUT_GROUP);
        Keyboard.on(Keyboard.keymap['MOVE_RIGHT'], partial(self.moveCharacter,1*self.size,0), CHARACTER_INPUT_GROUP);
        Keyboard.on(Keyboard.keymap['MOVE_LEFT'], partial(self.moveCharacter,-1*self.size,0), CHARACTER_INPUT_GROUP);
        Keyboard.on(Keyboard.keymap['MOVE_DOWN'], partial(self.moveCharacter,0,1*self.size), CHARACTER_INPUT_GROUP);
        Keyboard.on(Keyboard.keymap['MOVE_UP_RIGHT'], partial(self.moveCharacter,1*self.size,-1*self.size), CHARACTER_INPUT_GROUP);
        Keyboard.on(Keyboard.keymap['MOVE_UP_LEFT'], partial(self.moveCharacter,-1*self.size,-1*self.size), CHARACTER_INPUT_GROUP);
        Keyboard.on(Keyboard.keymap['MOVE_DOWN_RIGHT'], partial(self.moveCharacter,1*self.size,1*self.size), CHARACTER_INPUT_GROUP);
        Keyboard.on(Keyboard.keymap['MOVE_DOWN_LEFT'], partial(self.moveCharacter,-1*self.size,1*self.size), CHARACTER_INPUT_GROUP);


    ## character actions

    def moveCharacter(self, x, y, eventInfo):
        TurnManager.turn(120, lambda: self.move(x,y))

    def passTurn(self, eventInfo):
        TurnManager.turn(100)

    