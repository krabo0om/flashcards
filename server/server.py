import http

__author__ = 'pgenssler'

class FlashcardsServer(http.server.HTTPServer):
    def __init__(self, server_address, req_handler, cardhandler, config):
        super().__init__(server_address, req_handler)
        self.config = config
        self.cardhandler = cardhandler
