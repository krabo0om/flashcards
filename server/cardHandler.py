import json
import random
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
        self.box = []
        self.__init_box()
        self.current_card = None  # the current question is taken out of the box. if there is no answer
        # and the next question is asked, the first one vanishes

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
            print('loaded set {0} with {1} cards'.format(card_set.name, len(card_set.cards)))
        if len(self.sets) > 0:
            self.change_set(self.sets[0].name)

    def get_next_card(self):
        if len(self.sets) == 0:
            return None
        if self.current_set is None:
            self.change_set(self.sets[0].name)
        if self.current_card is not None:
            self.box[int(self.current_card.l_index) % 6].append(self.current_card)  # mod 6 because of compatibility

        for l in self.box:
            if len(l) > 0:
                c = l.pop(0)
                self.current_card = c
                return c
        return None

    def learned(self, level, card=None, cid=None):
        """ needs either card or cid (the card id) """
        if card is None:
            for c in self.current_set.cards:
                if c.id == cid:
                    card = c
                    break
        card.l_index = str(level)
        card.save(self.config)
        if int(level) == 0:
            self.box[0].insert(random.randrange(2, 4), card)  # put it back into pocket 0
        else:
            if len(self.box[int(level)]) == 0:
                self.box[int(level)].append(card)
            else:
                self.box[int(level)].insert(random.randrange(0, len(self.box[int(level)])),
                                            card)  # random into pocket x
        self.current_card = None
        return card.l_index

    def change_set(self, set_name):
        if self.current_set is not None and self.current_set.name == set_name:
            return set_name
        if len(self.sets) > 0:
            self.__init_box()  # clear box
            for s in self.sets:
                if s.name == set_name:
                    self.current_card = None
                    self.current_set = s  # set current card set
                    for c in self.current_set.cards:
                        self.box[int(c.l_index) % 6].append(c)  # place all cards in their pocket
                    for b in self.box:
                        random.shuffle(b)  # shuffle the cards in the boxes
                    return self.current_set.name
            return set_name + ' not found'
        else:
            return 'no sets loaded'

    def create_card(self, data):
        data = json.loads(data)
        card = Card()
        card.set = data['set']
        card.question = data['question']
        card.hint = data['hint']
        card.answer = data['answer']

        d_set = self.__find_set(card.set)
        if d_set is None:
            d_set = CardSet(card.set)
            self.sets.append(d_set)
        max_id = 0
        for c in d_set.cards:
            if int(c.id) >= int(max_id):
                max_id = int(c.id) + 1
        card.id = str(max_id)
        card.save(self.config)
        d_set.cards.append(card)
        return card.id

    def __find_set(self, set_name):
        """
        @rtype: CardSet
        """
        for s in self.sets:
            if s.name == set_name:
                return s
        return None

    def __init_box(self):
        self.box = []
        for i in range(6):
            self.box.append([])
