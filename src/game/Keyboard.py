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
    pass;


def on(keyEvents, fn, groupName=None):
    for keyEvent in keyEvents :
        Event.on(pygame.KEYDOWN, partial(handleKey, keyEvent, fn), groupName);
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



    