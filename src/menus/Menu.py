from src.game import TileService
from pygame import Surface
from pygame.sprite import Sprite

def getSurfaceDimsFromText(text, tileSize, width, height):
    return (
        len(text) * tileSize,
        tileSize
    )

class TileBorder():
    def __init__(self, tl, t, tr, l, r, bl, b, br):
        self.__dict__ = {
            'tl': tl,
            't': t,
            'tr': tr,
            'l': l,
            'r': r,
            'bl': bl,
            'b': b,
            'br': br
        }

    def __getitem__(self, key):
        return self.__dict__[key]

class FancyBorder(TileBorder):
    def __init__(self):
        TileBorder.__init__(self,
            tr=TileService.getTile((15,11)),
            t=TileService.getTile((4,12)),
            tl=TileService.getTile((10,13)),
            l=TileService.getTile((3,11)),
            r=TileService.getTile((3,11)),
            bl=TileService.getTile((0,12)),
            b=TileService.getTile((4,12)),
            br=TileService.getTile((9,13))
        )

class TextElement(Sprite):
    def __init__(self, text, sx, sy, w=-1, h=-1):
        Sprite.__init__(self)
        self.sx = sx
        self.sy = sy
        self.w = w
        self.h = h
        self.setText(text)
    
    def setText(self, text):
        self.text = text
        dims = getSurfaceDimsFromText(text, TileService.size, self.w, self.h)
        print('text dims', dims)
        print('sx', self.sx, 'sy', self.sy)
        self.image = Surface(dims)
        self.rect = (
            self.sx,
            self.sy,
            dims[0],
            dims[1]
        )
        blits = []
        x = 0
        y = 0
        for char in self.text:
            blits.append((TileService.getTileByChar(char), (x, y)))
            x += TileService.size
        self.image.blits(blit_sequence=blits)

class TileMenuFrame(Sprite):
    def __init__(self, sx, sy, w, h, camera, bgnd=None, brdr=None):
        Sprite.__init__(self)
        self.sx = sx
        self.sy = sy
        self.w = w
        self.h = h
        self.tw = int(w/TileService.size)
        self.th = int(h/TileService.size)
        if(bgnd is None):
            bgnd = TileService.getTile((0,0))
        if(brdr is None):
            brdr = TileService.getTile((11,13))
        self.background = bgnd
        self.border = brdr
        self.image = Surface((self.w, self.h))
        self.rect = (
            self.sx,
            self.sy,
            self.w,
            self.h
        )
        self.fill(self.background)
        self.addBorder(self.border)
        camera.add(self)

    def fill(self, tile):
        blits = []
        for y in range(0, self.th):
            for x in range(0, self.tw):
                blits.append((tile, (x*TileService.size, y*TileService.size)))
        self.image.blits(blit_sequence=blits)

    def addBorder(self, brdr):
        self.border = brdr
        if(self.border is not None):
            blits = []
            for y in range(0,self.th):
                for x in range(0,self.tw):
                    if(y == 0 or x == 0 or y == self.th-1 or x == self.tw-1):
                        blits.append((self.getBorderTile(x,y),(x*TileService.size,y*TileService.size)))
            self.image.blits(blit_sequence=blits)

    def getBorderTile(self, x, y):
        if(isinstance(self.border, dict) or isinstance(self.border, TileBorder)):
            if(y == 0 and x == 0):
                return self.border['tl'].copy()
            elif(y == 0 and x == self.tw-1):
                return self.border['tr'].copy()
            elif(y == 0 and x != self.tw-1):
                return self.border['t'].copy()
            elif(y == self.th-1 and x == 0):
                return self.border['bl'].copy()
            elif(y == self.th-1 and x == self.tw-1):
                return self.border['br'].copy()
            elif(y == self.th-1 and x != self.tw-1):
                return self.border['b'].copy()
            elif(y != self.th-1 and x == 0):
                return self.border['l'].copy()
            elif(y != self.th-1 and x == self.tw-1):
                return self.border['r'].copy()
            else:
                return TileService.getTile((0,0))
        else:
            return self.border


class TileMenu():
    def __init__(self, sx, sy, w, h, camera, bgnd=None, brdr=None):
        self.camera = camera
        self.sx = sx
        self.sy = sy
        self.w = w
        self.h = h
        frame = TileMenuFrame(sx, sy, w, h, self.camera, bgnd, brdr)
        self.elements = []
        self.addElement(frame)

    def addElement(self, element):
        self.elements.append(element)
        self.camera.add(element)

    def addText(self, text, ix=0, iy=0):
        sx = self.sx + TileService.size + ix
        sy = self.sy + TileService.size + iy
        textElement = TextElement(text, sx, sy, w=self.w)
        self.addElement(textElement)

    def addButton(self, text, ix=0, iy=0):
        pass
