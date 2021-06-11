import socket


class Socket:

    def __init__(self, credentials: 'TraderNetApi'):
        self._key = credentials._apikey
        self._secret = credentials._secret.encode()
        self.url = 'wsbeta.tradernet.ru'