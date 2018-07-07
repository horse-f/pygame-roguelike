print('scene router');

from src.game import Engine;

scenes = [];
scene = None;

def addScene(name, obj):
    global scenes;
    scenes.append({
        'name': name,
        'obj': obj
    });

def changeScene(sceneName):
    global scene;

    _scene = list(filter(lambda x: x['name'] == sceneName, scenes));

    if(len(_scene) == 1):
        if(scene is not None):
            scene.end();    

        scene = _scene[0]['obj'];
        scene.start();

def update():
    global scene;
    if(scene is not None) :
        scene.update();

def updateWorld() :
    global scene;
    if(scene is not None) :
        scene.updateWorld();

def load() :
    for _scene in scenes :
        _scene['obj'].load();