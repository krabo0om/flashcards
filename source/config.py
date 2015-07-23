import json
import os

__author__ = 'pgenssler'

class Config(object):
    def __init__(self, path=None):
        if path is None or not os.path.isfile(path):
            self.PATH_CARDS = '/home/pgenssler/lernkarten/cards/'
            self.port = 8000
        else:
            self.load(path)

    def load(self, path):
        if os.path.isfile(path):
            f = open(path, 'r')
            data = json.load(f)
            self.__dict__.update(data)

    def save(self, path):
        with open(path, 'w') as f:
            f.write(json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4))
