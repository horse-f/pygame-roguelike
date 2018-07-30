print('world');

from src.game import Event;
from src.game import SceneRouter;
from src.game import Keyboard;

from src.scene import Scene;
from src.character import Character;
from src.character import CharacterController;
from src.worldMap import WorldMap;

class World(Scene) :

    CHARACTER_GROUP = 'character_input_group';

    def __init__(self):
        Scene.__init__(self);
        self.paused = False;
        self.WorldMap = WorldMap();
        self.Character = CharacterController(Character(), self.CHARACTER_GROUP);

        Scene.add(self, 'CharacterController', self.Character);
        Scene.add(self, 'WorldMap', self.WorldMap);

        print('CharacterController', self.objects['CharacterController']);
        print('WorldMap', self.objects['WorldMap']);

        pass;


    def load(self):
        Scene.load(self);

        print('loading world');

        Keyboard.on(Keyboard.keymap['PAUSE'], self.pauseUnpause);

        pass;


    def start(self):
        Scene.start(self);

        print('starting world scene');

        self.WorldMap.buildMap();

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

