from pygame.sprite import Group
from src.game import SceneRouter

class GameObject(Group):
    def __init__(self, sizex, sizey, wx=0, wy=0):
        Group.__init__(self)
        self.wx = wx
        self.wy = wy
        self.sizex = sizex
        self.sizey = sizey
        self.scripts = []

    def move(self, wx, wy):
        self.wx += wx
        self.wy += wy
        for sprite in self:
            x = sprite.rect[0]
            y = sprite.rect[1]
            sprite.rect = (
                x + wx,
                y + wy,
                self.sizex,
                self.sizey
            )

    def addSprites(self, sprites, camera):
        self.add(sprites)
        camera.add(sprites)

    def removeSprites(self, sprites, camera):
        self.remove(sprites)
        camera.remove(sprites)

    def attachScript(self, script):
        self.scripts.append(script)

    def update(self, context={}, sprites=False):
        context['self'] = self
        if(sprites is True):
            Group.update(self)
        for script in self.scripts:
            script.update(context)
        

