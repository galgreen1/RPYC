import requests
from RPYC.server_constants import MODULE_REQUEST, MODULE_NAME, PROXY
from RPYC.proxy import Proxy
import json


class RemoteControlConnection:
    class Module:
        def __init__(self, base_url: str):
            self.base_url = base_url

        def __getattr__(self, name):
            response = requests.get(
                self.base_url + MODULE_REQUEST, data=json.dumps({MODULE_NAME: name})
            ).json()
            if type(response) is dict:
                if PROXY in response.keys():
                    return Proxy(int(response.get(PROXY)), self.base_url)
            return response

    def __init__(self, ip: str, port: int):
        self.modules = self.Module(f"http://{ip}:{port}")
