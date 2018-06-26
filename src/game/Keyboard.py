import pygame;
from src.game import Event;
from functools import partial;

def init() :
    pygame.key.set_repeat(500, 35);

def on(keyEvents, fn):
    for keyEvent in keyEvents :
        Event.on(pygame.KEYDOWN, partial(handleKey, keyEvent, fn));


def handleKey(keyEvent, callback, _event):
    if(keyEvent['key'] == _event.key and keyEvent['mod'] == _event.mod) :
        callback(_event);

    