print('Config');

from src.game import FS;

settings = {};
keyboardSettings = {};

def init():
    # look for settings in the folder
    # if no settings exist, output default settings
    pass;

def load():
    global settings;
    settings = FS.readJson('config/config.json');
    # parse settings, make sure all the required keys exist
    # if a key does not exist in the file, replace it in the settings with the default
    print('config is', settings);
    pass;




