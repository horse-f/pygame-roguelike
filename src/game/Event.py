print('Event');

import pygame.event;

handlers = [];

# use input groups to determine what handlers to call
#  this will allow for different modes of input processing
#   ex: for pausing the game, all the gameplay inputs would be under
#       the 'gameplay' group and a scene could enable or disable input
#       from that group and enable for another group like 'esc_menu' 
#       or 'inventory'

def on(event, fn) :
    handlers.append({
        'event': event,
        'func': fn
    });
    pass;

def digest() :
    global handlers;
    events = pygame.event.get();

    for _event in events :
        print('event', _event);

        for handler in handlers :

            if(handler['event'] == _event.type) : 
                handler['func'](_event);

    pass;

