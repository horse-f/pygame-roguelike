print('world');

from src.game import Engine;
from src.game import Render;
from src.game import SceneRouter;

from src.scene import Scene;
from src.character import Character;
from src.character import CharacterController;
from src.geometry import Geometry;

class World(Scene) : 

    def __init__(self):
        Scene.__init__(self);
        self.character = Character();
        self.characterController = CharacterController(self.character);

        self.geometry = Geometry();

    def load(self):
        print('loading world');
        self.characterController.load();
        self.geometry.load();

    def start(self):
        print('starting world scene');
        Render.add(self.character);
        Render.add(self.geometry);
        pass

    def end(self) :
        print('ending world scene');
        Render.remove(self.character);
        Render.remove(self.geometry);
        pass;

    def update(self):
        pass

    # def updateWorld(self):
    #     pass

print('adding world scene');
SceneRouter.addScene('game.World', World());

