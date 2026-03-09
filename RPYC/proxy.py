import requests
from RPYC.server_constants import ATTRIBUTE_REQUEST, CALL_REQUEST


class Proxy:
    def __init__(self, id: int, base_url: str):
        self.id = id
        self.base_url = base_url

    def __call__(self, *args, **kwds):
        return requests.get(
            self.base_url + CALL_REQUEST, data=[self.id, args, kwds]
        ).json()

    def __getattr__(self, name):
        return requests.get(
            self.base_url + ATTRIBUTE_REQUEST, data=[name, self.id]
        ).json()
