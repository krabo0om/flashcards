import json
import os

__author__ = 'pgenssler'

class Card(object):
    def __init__(self, path=None):
        if path is None:
            self.id = "999999"
            self.set = "test_set"
            self.question = "test?"
            self.hint = "hint"
            self.answer = "test!!"
            self.l_index = "0"
        else:
            self._load(path)

    def _load(self, path):
        if os.path.isfile(path):
            f = open(path, 'r')
            data = json.load(f)
            self.__dict__.update(data)

    def learn(self, stage):
        self.l_index = str(stage + int(self.l_index))

    def save(self, config):
        path = os.path.join(config.PATH_CARDS, self.set)
        if not os.path.exists(path):
            os.mkdir(path)
        path = os.path.join(path, self.id)

        with open(path, "w") as f:
            f.write(json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=4))

    def __str__(self):
        return self.question
