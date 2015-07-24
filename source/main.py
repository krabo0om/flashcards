
import sys
from cardHandler import CardHandler
from config import Config
from httpRequestHandler import myHandler
from server import FlashcardsServer

__author__ = 'pgenssler'

def start_server(card_handler, config):
    try:
        server = FlashcardsServer(('', config.port), myHandler, card_handler, config)
        print('Started http server')
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down server')
        server.socket.close()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: {0} <path to config>'.format(sys.argv[0]))
        exit(1)

    cfg_path = sys.argv[1]
    cfg = Config(cfg_path)
    c = CardHandler(cfg)
    c.load()
    print("loaded {0} sets".format(len(c.sets)))	
    start_server(c, cfg)
    cfg.save(cfg_path)
