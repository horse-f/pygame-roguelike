from src.game import Render;
from src.camera import Camera;

class Scene: 
    def __init__(self, cam=None):
        self.mainCamera = None;

        if(cam is None) :
            self.mainCamera = Camera();
        else :
            self.mainCamera = cam;

        self.objects = {};
        self.active = False;

        pass;


    def add(self, key, obj):
        self.objects[key] = obj;

        if(self.active) :
            Render.add(self.objects[key]);

        pass;


    def remove(self, key):
        if(key in self.objects) :
            if(self.active):
                Render.remove(self.objects[key]);

            del self.objects[key];

        pass;


    def update(self):
        self.mainCamera.snap(self.objects.values());

        for key in self.objects :
            self.objects[key].update();

        pass;


    def load(self):
        for key in self.objects :
            self.objects[key].load();

        pass;


    def start(self):
        self.active = True;
        for key in self.objects :
            Render.add(self.objects[key]);

        pass;


    def end(self):
        self.active = False;
        for key in self.objects :
            Render.remove(self.objects[key]);

        pass;