import hmac
import time


def nonce():
    return int(time.time() * 10000)


def create_sign(key, message):
    msg = _pre_sign(message).encode()
    return hmac.new(key=key, msg=msg, digestmod='sha256').hexdigest()


def _pre_sign(dict_: dict):
    result = []
    for key, value in dict_.items():
        if isinstance(value, dict):
            value = _pre_sign(value)
        result.append('%s=%s' % (key, value))
    return '&'.join(string for string in result)
