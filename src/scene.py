class Scene: 
    def __init__(self):
        pass

    ''' this gets run every frame once the program is initialized and loaded ''' 
    def update(self):
        pass

    ''' This is the update for the actual gameplay part of the game '''
    def updateWorld(self):
        pass

    ''' this is run after all the packages have been initialized '''
    ''' meant for loading images and other assets '''
    def load(self):
        pass

    ''' this is called when the scene gets changed to '''
    def start(self):
        pass

    ''' this gets called right before the scene is changed '''
    def end(self):
        pass