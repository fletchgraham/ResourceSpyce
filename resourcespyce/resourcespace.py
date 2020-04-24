import requests
import hashlib

class ResourceSpace:
    def __init__(self, base_url='', user='admin', private_key=''):
        self.base_url = base_url
        self.user = user
        self.private_key = private_key

    def do_search(self, param1):
        query = f'user={self.user}&function=do_search&param1={param1}'
        sign = hashlib.sha256(
            f'{self.private_key}{query}'.encode()
            ).hexdigest()

        res = requests.get(f'{self.base_url}{query}&sign={sign}')

        return res.json()
