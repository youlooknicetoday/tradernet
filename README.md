<div style="text-align:center">Русский | <a href=https://github.com/youlooknicetoday/tradernet/tree/master/lang/english> English</a></div>

Данный модуль явлется оберктой вокруг API TraderNet

https://tradernet.ru/

# Пример использования
Инициализация параметров может быть осуществлена из файла конфига, лежащего рядом со скриптом
```python
from tradernet import TraderNetAPI
from tradernet.config import read_config

api = TraderNetAPI(read_config('api.ini'))
```
Или можно напрямую передать в экземпляр
```python
api = TraderNetAPI((public, secret))
```
И дальше использовать методы API
```python
data = api.v2.send_request(
    'getSecurityInfo', params={'ticker': 'SBER'}
)
```

## Документация

Документация для методов v1 и socket находится здесь:

https://github.com/tradernet/tn.api

Возможные методы v2 могут быть найдены здесь

https://tradernet.ru/tradernet-api/public-api-client

