from src.game import Render;
from copy import copy;

class Camera:
    def __init__(self):

        self.center = {
            'x': 0,
            'y': 0
        };
        # self.oldCenter = copy(self.center);

        pass;

    def setCenter(self, x, y):
        self.center = {
            'x': x,
            'y': y
        };
        # self.oldCenter = copy(self.center);

        pass;

    def snap(self, objects):
        # if(self.oldCenter['x'] != self.center['x'] and self.oldCenter['y'] != self.center['y']) :

        cx = Render.display.get_width()/2;
        cy = Render.display.get_height()/2;

        deltaX = cx - self.center['x'];
        deltaY = cy - self.center['y'];

        for obj in objects: 
            obj.rect = (
                obj.pos['x'] + deltaX,
                obj.pos['y'] + deltaY,
                obj.size,
                obj.size
            );

        print('taking snapshot');

        pass;

    def draw(self):
        pass;