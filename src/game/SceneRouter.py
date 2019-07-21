print('scene router');

# from src.game import Engine;

# scenes = [];
scene = None;

# def addScene(name, obj):
#     global scenes;
#     scenes.append({
#         'name': name,
#         'obj': obj
#     });

#     pass;


# def changeScene(sceneName):
#     global scene;
    
#     if(scene is not None):
#         scene.end();    

#     _scene = list(filter(lambda x: x['name'] == sceneName, scenes));

#     if(len(_scene) >= 1):

#         scene = _scene[0]['obj'];
#         scene.start();

def changeTo(_scene):
    global scene
    if(scene is not None):
        scene.end()
    scene = _scene
    scene.start()

def update():
    global scene
    if(scene is not None) :
        scene.update()

def getScene():
    global scene
    return scene