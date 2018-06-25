print('Event');

import pygame.event;

handlers = [];

def on(event, fn) :
    handlers.append({
        'event': event,
        'func': fn
    });

def digest() :
    events = pygame.event.get();

    for _event in events :
        # print('event', _event);

        for handler in handlers :

            if(handler['event'] == _event.type) : 
                handler['func'](_event);
