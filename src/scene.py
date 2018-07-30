from src.game import Render;
from src.camera import Camera;

class Scene: 
    def __init__(self, cam=None):
        self.mainCamera = None;

        if(cam is None) :
            self.mainCamera = Camera();
        else :
            self.mainCamera = cam;

        Render.camera = self.mainCamera;

        self.objects = {};
        self.active = False;

        pass;

    def setCamera(cam) :
        self.mainCamera = cam;

        Render.camera = self.mainCamera;

        pass;

    def add(self, key, obj):
        self.objects[key] = obj;

        if(self.active) :
            self.mainCamera.add(self.objects[key]);

        pass;


    def remove(self, key):
        if(key in self.objects) :
            if(self.active):
                self.mainCamera.remove(self.objects[key]);

            del self.objects[key];

        pass;


    def update(self):

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
            self.mainCamera.add(self.objects[key]);

        pass;


    def end(self):
        self.active = False;
        for key in self.objects :
            self.mainCamera.remove(self.objects[key]);

        pass;