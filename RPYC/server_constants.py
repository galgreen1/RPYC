#  URLS available in the server
MODULE_REQUEST = "/module"
ATTRIBUTE_REQUEST = "/attribute"
CALL_REQUEST = "/call"

PROXY = "proxy"
MODULE_NAME = "module_name"
PROXY_ID = "proxy_id"
ATTRIBUTE_NAME = "attribute"
ARGS = "args"
KWARGS = "kwargs"

NON_VALID_MODULE_NAME = "non valid module name"
NON_VALID_PROXY_ID = "non valid proxy id"
NON_VALID_ATTRIBUTE_NAME = "non valid attribute name"
NON_VALID_ARGS = "non valid args"
NON_VALID_KWARGS = "non valid kwargs"

#  All of the varible types that are considered simple
#  Simple varibles will be returned simply,
#  while other types will be retured by refrence only
SIMPLE_TYPES = [int, float, str, None, bool]
