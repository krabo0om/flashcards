import http.client
import json
from card import Card

__author__ = 'pgenssler'


class FlashcardsClientAPI(object):
    PATH_NEXT_CARD = 'nxtc'
    PATH_CURRENT_SET = 'gset'
    PATH_SET_SET = 'sset'
    PATH_ALL_SETS = 'gsets'
    PATH_LEARNED = 'learned'
    PATH_NEW_CARD = 'ncard'

    def __init__(self, host, port):
        """
        @param host: the host address
        @param port: port on the host
        @return: a new api instance
        """
        self.host = host
        self.port = port
        self.connection = http.client.HTTPConnection(host, port=int(port))
        self.headers = {'Content-type': 'text/plain'}

    def __conn(self, method, path, data):
        """
        @param method: get/put/post ...
        @param path: the path on the host
        @param data: data to send
        @return: received data
        @rtype : str
        """
        self.connection.request(method, path, data, self.headers)
        rsp = self.connection.getresponse()
        return rsp.readall().decode('utf-8')

    def _get(self, path):
        """
        get request to the server
        @param path: the path on the host
        @return: received data from the host
        @rtype : str
        """
        return self.__conn('GET', path, '')

    def _post(self, path, data):
        """
        send data to the server
        @param path: path on the server
        @param data: data to send to the server
        @return: answer from the server
        @rtype: str
        """
        return self.__conn('POST', path, data)

    def get_all_sets(self):
        """
        gets the sets available from the server
        @return: a list of those sets
        @rtype: list of str
        """
        return self._get(self.PATH_ALL_SETS).split(',')

    def get_current_set(self):
        """
        gets the currently selected set
        @return: the current set
        @rtype: str
        """
        return self._get(self.PATH_CURRENT_SET)

    def get_next_card(self):
        """
        asks for the next card from the current set
        @return: the next card
        @rtype: Card
        """
        c = Card()
        c.__dict__.update(json.loads(self._get(self.PATH_NEXT_CARD)), encoding='utf-8')
        return c

    def set_set(self, set_name):
        """
        changes the selected set
        @param set_name: the new name of the set, if it does not exist, the set won't change
        @return: the set of the current set
        @rtype: str
        """
        return self._post(self.PATH_SET_SET, set_name)

    def answer(self, card_id, level):
        """
        sends the improvement to the server
        @param card_id: the id of the learned card
        @param level: number between 0 (what the???) and 5 (that wasn't a question!!)
        @return: the new level of that card
        @rtype: int
        """
        data = json.dumps({'id': str(card_id), 'level': str(level)})
        return int(self._post(self.PATH_LEARNED, data))

    def create_card(self, set_name, question, hint, answer):
        """
        creates a new card
        @param set_name: the set to insert the card to
        @param question: the new question
        @param hint: a simple hint
        @param answer: the whole answer
        @return: the id of the new card
        @rtype: str
        """
        data = json.dumps({'set': set_name, 'question': question, 'hint': hint, 'answer': answer})
        return self._post(self.PATH_NEW_CARD, data)

