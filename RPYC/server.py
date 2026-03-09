from flask import Flask, request
from RPYC.server_constants import (
    ATTRIBUTE_REQUEST,
    CALL_REQUEST,
    MODULE_REQUEST,
    PROXY,
    SIMPLE_TYPES,
    MODULE_NAME,
    NON_VALID_MODULE_NAME,
    PROXY_ID,
    ATTRIBUTE_NAME,
    NON_VALID_ATTRIBUTE_NAME,
    NON_VALID_PROXY_ID,
    NON_VALID_ARGS,
    NON_VALID_KWARGS,
    ARGS,
    KWARGS,
)
import importlib
from typing import Dict
import json


app = Flask(__name__)
PROXY_MAPPING: Dict[int, object] = {}


def generate_proxy_id() -> int:
    """
    Generates a unique id that isnt taken
    """
    id = len(PROXY_MAPPING)
    while id in PROXY_MAPPING.keys():
        id *= 2
    return id


@app.route(ATTRIBUTE_REQUEST, methods=["GET"])
def get_attr():
    request_json = json.loads(request.data)
    proxy_id = request_json.get(PROXY_ID)
    if proxy_id is None:
        raise Exception(NON_VALID_PROXY_ID)
    attribute = request_json.get(ATTRIBUTE_NAME)
    if not attribute:
        raise Exception(NON_VALID_ATTRIBUTE_NAME)
    attr = getattr(PROXY_MAPPING.get(int(proxy_id)), attribute)
    if type(attr) not in SIMPLE_TYPES:
        attr_id = generate_proxy_id()
        PROXY_MAPPING[attr_id] = attr
        return json.dumps({PROXY: attr_id})
    return json.dumps(attr)


@app.route(CALL_REQUEST, methods=["GET"])
def call():
    request_json = json.loads(request.data)
    proxy_id = int(request_json.get(PROXY_ID))
    if proxy_id is None:
        raise Exception(NON_VALID_PROXY_ID)
    args = request_json.get(ARGS)
    if args is None:
        raise Exception(NON_VALID_ARGS)
    kwargs = request_json.get(KWARGS)
    print(args, kwargs)
    if kwargs is None:
        raise Exception(NON_VALID_KWARGS)
    call_result = PROXY_MAPPING.get(proxy_id)(*args, **kwargs)
    if type(call_result) not in SIMPLE_TYPES:
        attr_id = generate_proxy_id()
        PROXY_MAPPING[attr_id] = call_result
        return json.dumps({PROXY: attr_id})
    return json.dumps(call_result)


@app.route(MODULE_REQUEST, methods=["GET"])
def get_module():
    request_json = json.loads(request.data)
    module_name = request_json.get(MODULE_NAME)
    if not module_name:
        raise Exception(NON_VALID_MODULE_NAME)
    module = importlib.import_module(module_name)
    if type(module) not in SIMPLE_TYPES:
        module_id = generate_proxy_id()
        PROXY_MAPPING[module_id] = module
        return json.dumps({PROXY: module_id})
    return json.dumps(module)
