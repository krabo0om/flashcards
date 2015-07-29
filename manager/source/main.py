import sys
from client_api import FlashcardsClientAPI
from source.gui_main import vp_start_gui

__author__ = 'pgenssler'

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('usage: {0} <host> <port>'.format(sys.argv[0]))
        exit(1)

    api = FlashcardsClientAPI(sys.argv[1], sys.argv[2])

    vp_start_gui(api)
