import requests
import json
from RPYC.server_constants import (
    ATTRIBUTE_REQUEST,
    CALL_REQUEST,
    ATTRIBUTE_NAME,
    PROXY_ID,
    ARGS,
    KWARGS,
    PROXY,
)


class Proxy:
    def __init__(self, id: int, base_url: str):
        self.id = id
        self.base_url = base_url

    def __call__(self, *args, **kwds):
        response = requests.get(
            self.base_url + CALL_REQUEST,
            data=json.dumps({PROXY_ID: self.id, ARGS: args, KWARGS: kwds}),
        ).json()
        if type(response) is dict:
            if PROXY in response.keys():
                return Proxy(response.get(PROXY), self.base_url)
        return response

    def __getattr__(self, name):
        response = requests.get(
            self.base_url + ATTRIBUTE_REQUEST,
            data=json.dumps({ATTRIBUTE_NAME: name, PROXY_ID: self.id}),
        ).json()
        if type(response) is dict:
            if PROXY in response.keys():
                return Proxy(response.get(PROXY), self.base_url)
        return response
