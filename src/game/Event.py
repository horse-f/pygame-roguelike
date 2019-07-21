print('Event');

import pygame.event;

inputGroups = {
    'MAIN': {
        'active': True,
        'handlers': []
    }
};


def on(event, fn, groupName=None) :
    global inputGroups;
    group = 'MAIN';

    if(groupName is not None) :
        group = groupName;

    if(group not in inputGroups) :
        inputGroups[group] = { 
            'active': True,
            'handlers': []
        };
        
    inputGroups[group]['handlers'].append({
        'event': event,
        'func': fn
    });


def digest() :
    events = pygame.event.get();

    for _event in events :
        # print('event', _event);

        for groupName in inputGroups :
            group = inputGroups[groupName];

            if(group['active']):
                runHandlers(group['handlers'], _event);


def runHandlers(_handlers, _event):

    for handler in _handlers :
        if(handler['event'] == _event.type) : 
            handler['func'](_event);


def setActive(groupName, active):
    global inputGroups;

    if(groupName in inputGroups) :
        inputGroups[groupName]['active'] = active;


