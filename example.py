from tradernet import TraderNetAPI
from tradernet.config import read_config

# api = TraderNetAPI((public, secret))
api = TraderNetAPI(read_config())
data = api.v2.send_request('getSecurityInfo', params={'ticker': 'SBER'})
print(data)
