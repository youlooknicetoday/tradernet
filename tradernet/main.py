from .src.versions import Version2
from .config import load_config
import httpx


class Worker:
    def __init__(self, *, apikey, secret):
        self._ctx = apikey, secret
        self._session = httpx.Client(base_url='https://tradernet.ru/api/')
        self.v2 = Version2(self._ctx, self._session)

    @classmethod
    def from_config(cls, path):
        config = load_config(path)
        return cls(**config.representation)
