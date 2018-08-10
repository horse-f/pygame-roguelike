import json;

def readJson(path):
    with open(path) as f:
        return json.load(f);
