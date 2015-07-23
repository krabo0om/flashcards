
import http.server
from card import Card
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
    cfg = Config('config.json')
    c = CardHandler(cfg)
    c.load()
    start_server(c, cfg)
    cfg.save('config.json')
