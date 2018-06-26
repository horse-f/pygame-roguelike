print('Config');

settings = {};
keyboardSettings = {};

def init():
    global settings;
    settings['tileSheet'] = 'assets/tiles.png';
    loadSettings();
    loadKeyboard();

def loadSettings():
    global settings;
    print('********** load settings');

def loadKeyboard():
    global keyboardSettings;
    print('********** load keyboard');

