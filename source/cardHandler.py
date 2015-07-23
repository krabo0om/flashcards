import os
from card import Card

__author__ = 'pgenssler'

class CardSet(object):
    def __init__(self, name):
        self.name = name
        self.cards = []

    def __str__(self):
        return self.name

class CardHandler(object):
    def __init__(self, config):
        self.sets = []
        self.current_set = None
        self.config = config

    def load(self):
        self.sets = []
        for s in os.listdir(self.config.PATH_CARDS):
            card_set = CardSet(s)
            self.sets.append(card_set)
            path = os.path.join(self.config.PATH_CARDS, s)
            for c in os.listdir(path):
                c_abs = os.path.join(self.config.PATH_CARDS, s, c)
                card = Card(c_abs)
                card_set.cards.append(card)
        self.current_set = self.sets[0]

    def get_next_card(self):
        if len(self.sets) == 0:
            return None
        if self.current_set is None:
            self.current_set = self.sets[0]
        min_v = 999999
        card = None
        for c in self.current_set.cards:
            if int(c.l_index) < min_v:
                card = c
                min_v = int(c.l_index)
        return card

    """ needs either card or cid (the card id) """
    def learned(self, level, card=None, cid=None):
        if card is None:
            for c in self.current_set.cards:
                if c.id == cid:
                    card = c
        card.l_index = str(int(card.l_index) + int(level))
        card.save(self.config)
        return card.l_index

    def change_set(self, set_name):
        for s in self.sets:
            if s.name == set_name:
                self.current_set = self.sets[set_name]
        return self.current_set.name
