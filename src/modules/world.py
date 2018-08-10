print('world');

from src.game import Event;
from src.game import SceneRouter;
from src.game import Keyboard;

from src.scene import Scene;

from src.modules.map import Map;
from src.modules.character import Character;
from src.modules.character import CharacterController;

class World(Scene) :

    CHARACTER_GROUP = 'character_input_group';

    def __init__(self):
        Scene.__init__(self);
        self.paused = False;
        self.Character = CharacterController(Character(), self.CHARACTER_GROUP);
        self.TestMap = Map();

        Scene.add(self, 'CharacterController', self.Character);
        Scene.add(self, 'TestMap', self.TestMap);

        pass;


    def load(self):
        Scene.load(self);

        print('loading world');
        self.TestMap.loadMap('pygame-roguelike-layout-01');

        Keyboard.on(Keyboard.keymap['PAUSE'], self.pauseUnpause);

        pass;


    def start(self):
        Scene.start(self);

        print('starting world scene');

        pass;


    def end(self) :
        Scene.end(self);

        print('ending world scene');

        pass;


    def update(self):
        Scene.update(self);

        self.mainCamera.focus(self.Character.character.pos);

        pass;


    def pauseUnpause(self, eventInfo):

        self.paused = not self.paused;
        Event.change(self.CHARACTER_GROUP, not self.paused);

        pass;


print('adding world scene');
SceneRouter.addScene('game.World', World());
SceneRouter.changeScene('game.World');

