import requests
from RPYC.server_constants import MODULE_REQUEST


class RemoteControlConnection:
    class Module:
        def __init__(self, base_url: str):
            self.base_url = base_url

        def __getattr__(self, name):
            return requests.get(self.base_url + MODULE_REQUEST, data=name).json()

    def __init__(self, ip: str, port: int):
        self.modules = self.Module(f"https://{ip}/{port}")
