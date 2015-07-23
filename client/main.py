import http.client
import json

__author__ = 'pgenssler'


def get(path):
    connection = http.client.HTTPConnection('localhost', port=8000)
    headers = {'Content-type': 'text/plain'}
    connection.request('GET', path, '', headers)
    rsp = connection.getresponse()
    connection.close()
    return rsp.readall().decode('utf-8')

def post(path, data):
    connection = http.client.HTTPConnection('localhost', port=8000)
    headers = {'Content-type': 'text/plain'}
    connection.request('POST', path, data, headers)
    rsp = connection.getresponse()
    connection.close()
    return rsp.readall().decode('utf-8')

if __name__ == '__main__':
    # set a set
    sets = get('gsets')
    ui = input('select a set: ' + sets + '\n')
    print('current set: ' + post('sset', ui))
    card = json.loads(get('nxtc'))
    ui = input('answer: ' + card['question'] + ' ')
    lvl = 0
    if ui == card['answer']:
        lvl = input('correct, level: ')
    else:
        print("fail. correct: " + card['answer'] + "\nlevel increase: 0")

    cid = card['id']
    data = '{"id":"%s", "level": "%s"}' % (cid, str(lvl))
    lvl = post('learned', data)
    print('new level: ' + lvl)
