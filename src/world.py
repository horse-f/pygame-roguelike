print('world');

from src.game import Engine;
from src.game import Render;
from src.game import SceneRouter;
from src.game import Keyboard;

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
        pass;

    def load(self):
        print('loading world');
        Scene.load(self);

        Keyboard.on(Keyboard.keymap['PAUSE'], self.pauseScene);

        self.characterController.load();
        self.geometry.load();
        pass;

    def start(self):
        print('starting world scene');
        Scene.start(self);

        Render.add(self.character);
        Render.add(self.geometry);
        pass;

    def end(self) :
        print('ending world scene');
        Scene.end(self);

        Render.remove(self.character);
        Render.remove(self.geometry);
        pass;

    def update(self):
        Scene.update(self);

        self.characterController.update();
        self.geometry.update();
        pass;

    def pauseScene(self):
        print('should pause');
        pass


print('adding world scene');
SceneRouter.addScene('game.World', World());

