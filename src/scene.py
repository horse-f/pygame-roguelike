class Scene: 
    def __init__(self):
        self.objects = {};
        pass

    def add(key, obj):
        objects[key] = obj;
        pass;

    ''' this gets run every frame once the program is initialized and loaded ''' 
    def update(self):
        pass;

    ''' this is run after all the packages have been initialized '''
    ''' meant for loading images and other assets '''
    def load(self):
        pass;

    ''' this is called when the scene gets changed to '''
    def start(self):
        pass;

    ''' this gets called right before the scene is changed '''
    def end(self):
        pass;