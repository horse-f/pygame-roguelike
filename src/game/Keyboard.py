import pygame;
from src.game import Event;
from functools import partial;
from src.game import FS;

keymap = {};

def init() :
    pygame.key.set_repeat(500, 35);

def load():
    global keymap;
    keymap = FS.readJson('config/keyboard.json');
    print('keys are', keymap);

def on(keyEvents, fn):
    for keyEvent in keyEvents :
        Event.on(pygame.KEYDOWN, partial(handleKey, keyEvent, fn));

def handleKey(keyEvent, callback, _event):
    if(keyEvent['key'] == _event.key and keyEvent['mod'] == _event.mod) :
        callback(_event);

''' looks for the event on the queue '''
def ifKeys(keys, callback):
    # look into the events there
    # if the event matches the key event
    # then hit the callback
    pass

    