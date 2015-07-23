from http.server import BaseHTTPRequestHandler
import json

__author__ = 'pgenssler'


class myHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        path = self.path.replace('/', '', 1)
        if path == '':
            self.print_api()
        elif path == 'nxtc':
            self.send_complete_header('application/json')
            card = self.server.cardhandler.get_next_card()
            self.wfile_write(str(json.dumps(card, default=lambda o: o.__dict__, sort_keys=True, indent=4)))
        elif path == 'gset':
            self.send_complete_header('text/plain')
            self.wfile_write(str(self.server.cardhandler.current_set))
        elif path == 'gsets':
            self.send_complete_header('text/plain')
            formatted = '%s' % (','.join(str(it) for it in self.server.cardhandler.sets))
            self.wfile_write(formatted)

    def do_POST(self):
        path = self.path.replace('/', '', 1)
        data = self.rfile.read(int(self.headers.get('Content-Length'))).decode("utf-8")
        if path == '':
            self.print_api()

        elif path == 'learned':
            self.send_complete_header('text/plain')
            pair = json.loads(data)
            if 'id' in pair and 'level' in pair:
                lvl = self.server.cardhandler.learned(pair['level'], cid=pair['id'])
                self.wfile_write(str(lvl))
            else:
                self.wfile_write('-1')

        elif path == 'sset':
            self.send_complete_header('text/plain')
            cs = self.server.cardhandler.change_set(data)
            self.wfile_write(cs)

    def wfile_write(self, text, encoding='utf-8'):
        self.wfile.write(text.encode(encoding))

    def send_complete_header(self, res_type):
        self.send_response(200)
        self.send_header('Content-type', res_type)
        self.end_headers()

    def print_api(self):
        self.send_complete_header('text/html')
        self.wfile_write('<html><head><title>flash cards api</title></head>')
        self.wfile_write('<body><p>flashcards api:</p><p><ul>')
        self.wfile_write('<li>get the next cards as json: get request on path nxtc</li>')
        self.wfile_write(
            '<li>post result for a card id: post on path learned with json { "id":"card_id", "level": increase"},'
            'returns the new level</li>')
        self.wfile_write('<li>get current set as string: get on path gset</li>')
        self.wfile_write('<li>get all sets as comma string: get on path gsets</li>')
        self.wfile_write('<li>change current set: post on path sset with name of set</li>')
        self.wfile_write('</ul></p></body></html>')
