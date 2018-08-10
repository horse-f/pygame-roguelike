print('Objects');

from src.game import FS;
from glob import glob;
import os;
from copy import copy;

objects = {};

def init(_dir='objects'):
    global objects;
    print('init objects');

    _glob = os.path.join(os.getcwd(), _dir, '**', '*.json');

    fileNames = glob(_glob, recursive=True);



    for fileName in fileNames:
        _json = FS.readJson(fileName);
        _cat = _json.pop('category', None);

        if(_cat is not None) :

            if(_cat not in objects):
                objects[_cat] = [];

            objects[_cat].append(copy(_json));

    pass;