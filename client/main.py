import sys

from fc_common.client_api import FlashcardsClientAPI

__author__ = 'pgenssler'

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('usage: {0} <host> <port>'.format(sys.argv[0]))
        exit(1)

    host = sys.argv[1]
    port = sys.argv[2]

    api = FlashcardsClientAPI(host, port)

    sets = api.get_all_sets()
    ui = input('select a set: ' + ', '.join(sets) + '\n')
    print('current set: ' + api.set_set(ui))
    card = api.get_next_card()
    ui = input('answer: ' + card.question + '\n')
    lvl = 0
    if ui == card.answer:
        lvl = input('correct, level: ')
        lvl = api.answer(card.id, lvl)
        print('new level: ' + str(lvl))
    else:
        print("fail. correct: " + card.answer + "\nlevel increase: 0")
