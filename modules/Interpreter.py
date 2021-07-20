
TOKEN_INTEGER = b'i'
TOKEN_LIST = b'l'
TOKEN_DICT = b'd'
TOKEN_END = b'e'
TOKEN_STRING_SEPARATOR = b':'

class Interpreter:
    _data = ""
    _index = 0
    def __init__(self):
        pass
    def decode(self, data:bytes):
        if not isinstance(data,bytes):
            raise TypeError(f'Decode failed, wrong data format. Received {type(data)}')
        self._data = data
        self._index = 0
        message = []
        while self._index < len(self._data):
            c = self._peek()
            if c == TOKEN_INTEGER:
                message.append(self._decode_number())
            self._step()
        return message
    def _decode_number(self):
        result = b''
        n = self._peek()
        while n != TOKEN_END and n is not None:
            if n in b'0123456789-':
                result += n
            self._step()
            n = self._peek()
        return int(result)
    def _step(self):
        self._index += 1
    def _peek(self):
        if self._index > len(self._data):
            return None
        return self._data[self._index:self._index+1]

    def encode(self):
        pass
