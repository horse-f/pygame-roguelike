from src.game import Render;

class Scene: 
    def __init__(self):
        self.objects = {};

        pass

    def add(self, key, obj):
        self.objects[key] = obj;
        # need to add to the render group if scene is active

        pass;

    def remove(self, key):
        # remove from scene objects 
        # remove object from render group if scene is active

        pass;

    ''' this gets run every frame once the program is initialized and loaded ''' 
    def update(self):
        for key in self.objects :
            self.objects[key].update();

        pass;

    ''' this is run after all the packages have been initialized '''
    ''' meant for loading images and other assets '''
    def load(self):
        for key in self.objects :
            self.objects[key].load();

        pass;

    ''' this is called when the scene gets changed to '''
    def start(self):
        for key in self.objects :
            Render.add(self.objects[key]);

        pass;

    ''' this gets called right before the scene is changed '''
    def end(self):
        for key in self.objects :
            Render.remove(self.objects[key]);

        pass;