import logging
import requests

from .exceptions import dispatcher
from .sign import nonce, create_sign
from .utils import http_build_query, recursive_sort


logger = logging.getLogger(__name__)


class Version2:

    def __init__(self, credentials: 'TraderNetApi'):
        self._key = credentials._apikey
        self._secret = credentials._secret.encode()
        self.url = 'https://tradernet.ru/api/v2/cmd/'
        self.init_credentials()

    def init_credentials(self):
        result = self.send_request('getAuthInfo')
        success = result.get('auth_login')
        if success:
            self.__class__.established = True
            logger.info('Hello, %s!', success)
            return
        print("Can't connect to server")

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
        data = requests.post(f'{self.url}{method}', headers=headers, data=data).json()
        if message := data.get('errMsg'):
            exception_code = data['code']
            raise dispatcher[exception_code](message)
        return data
