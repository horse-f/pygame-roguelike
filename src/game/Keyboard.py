import pygame;
from src.game import Event;
from functools import partial;
from src.game import FS;

keymap = {};

def init() :
    pygame.key.set_repeat(500, 35);


def load():
    global keymap;
    keymap = mapKeys(FS.readJson('config/keyboard.json'));
    print('keys are', keymap);
    pass;


def on(keyEvents, fn):
    print('keyboard on', keyEvents, fn);
    for keyEvent in keyEvents :
        Event.on(pygame.KEYDOWN, partial(handleKey, keyEvent, fn));
    pass;


def handleKey(keyEvent, callback, _event):
    if(keyEvent['key'] == _event.key and keyEvent['mod'] == _event.mod) :
        callback(_event);
    pass;


def mapKeys(keys):
    mappedKeys = {};

    for key in keys:
        mappedKeys[key] = list(map(parseKeyDict, keys[key]));

    return mappedKeys;


def parseKeyDict(keyDict):
    return {
        'mod': getattr(pygame, keyDict['mod']),
        'key': getattr(pygame, keyDict['key'])
    };



    