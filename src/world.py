print('world');

from src.game import Engine;
from src.game import Event;
from src.game import Render;
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

        Scene.add(self, 'CharacterController', CharacterController(Character(), self.CHARACTER_GROUP));
        Scene.add(self, 'WorldMap', WorldMap());

        print('CharacterController', self.objects['CharacterController']);
        print('WorldMap', self.objects['WorldMap']);

        pass;


    def load(self):
        print('loading world');

        Scene.load(self);

        Keyboard.on(Keyboard.keymap['PAUSE'], self.pauseUnpause);

        pass;


    def start(self):
        print('starting world scene');

        Scene.start(self);
        print('sprites', Render.renderGroup.sprites());

        self.objects['WorldMap'].buildMap();
        
        print('sprites', Render.renderGroup.sprites());

        pass;


    def end(self) :
        print('ending world scene');

        Scene.end(self);

        pass;


    def update(self):

        Scene.update(self);

        pass;


    def pauseUnpause(self, eventInfo):

        self.paused = not self.paused;
        Event.change(self.CHARACTER_GROUP, not self.paused);

        pass;


print('adding world scene');
SceneRouter.addScene('game.World', World());

