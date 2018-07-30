from src.game import Render;
# from copy import copy;

class Camera:
    def __init__(self):

        self.objects = [];
        self.center = {
            'x': 0,
            'y': 0
        };

        pass;


    def focus(self, pos):

        self.center = {
            'x': pos['x'],
            'y': pos['y']
        };

        self.offset();

        pass;


    def draw(self, display):
        for obj in self.objects:
            obj.draw(display);

        pass;


    def add(self, obj):
        self.objects.append(obj);

        pass;

    def remove(self, obj):
        if(obj in self.objects):
            self.objects.remove(obj);

        pass;


    def offset(self):
        cx = Render.display.get_width()/2;
        cy = Render.display.get_height()/2;

        for obj in self.objects:
            sprites = obj.sprites();

            for sprite in sprites:
                nx = cx - (self.center['x'] - sprite.pos['x']);
                ny = cy - (self.center['y'] - sprite.pos['y']);

                sprite.rect = (
                    nx,
                    ny,
                    sprite.size,
                    sprite.size
                );

        pass;
