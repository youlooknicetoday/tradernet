<p align="center"><a href=https://github.com/youlooknicetoday/tradernet> Русский </a>| English</p>

This module provides simple operations with API TraderNet

https://tradernet.ru/

# Simple Usage
```python
from tradernet import TraderNetAPI

api = TraderNetAPI.from_config('api.ini')
```
or you can pass credentials directly
```python
api = TraderNetAPI((public, secret))
```
And then use it
```python
data = api.v2.send_request(
    'getSecurityInfo', params={'ticker': 'SBER'}
)
```

## Documentation

You can find documentation for v1 api methods and socket here (russian):

https://github.com/tradernet/tn.api

Possible v2 api methods could be found there:

https://tradernet.ru/tradernet-api/public-api-client