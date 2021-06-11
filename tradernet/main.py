from .src.versions import Version2


class Worker:
    def __init__(self, connection):
        self._apikey, self._secret = connection
        self.v2 = Version2(self)
