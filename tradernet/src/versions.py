import logging
import httpx

from .sign import nonce, create_sign
from .utils import http_build_query, recursive_sort


logger = logging.getLogger(__name__)


class Version2:

    def __init__(self, context: tuple[str, str], session: httpx.Client):
        self._key, self._secret = context
        self._secret = self._secret.encode()
        self._session = session

    def send_request(self, method, params: dict = None):
        data = {'apiKey': self._key, 'cmd': method, 'nonce': nonce()}
        if params:
            data['params'] = params
        data = recursive_sort(data)
        headers = {
            'X-NtApi-Sig': create_sign(self._secret, data),
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = http_build_query(data)
        data = self._session.post('v2/cmd/%s' % method, headers=headers, data=data).json()
        if message := data.get('errMsg'):
            raise Exception(message)
        return data
