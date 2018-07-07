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

    pass;


def changeScene(sceneName):
    global scene;
    
    if(scene is not None):
        scene.end();    

    _scene = list(filter(lambda x: x['name'] == sceneName, scenes));

    if(len(_scene) >= 1):

        scene = _scene[0]['obj'];
        scene.start();

    pass;


def update():
    global scene;
    if(scene is not None) :
        scene.update();

    pass;


def load() :
    for _scene in scenes :
        _scene['obj'].load();

    pass;
