from configparser import ConfigParser
from baseSettings import application_path
import os

FILE = os.path.join(application_path, "config.ini")


def get_tm1_config(instance: str) -> dict:
    """
    Read in config.ini, attach username and password
    :param instance: TM1 Section name from config file
    :return: dict of values needed for TM1PY
    """
    _user = None
    _pass = None
    base_url = None
    address = None
    port = None
    gateway = None
    namespace = None
    ssl = False
    config = ConfigParser()
    config.read(FILE)
    conf = dict(config.items(instance))
    _cloud = str_to_bool(conf['cloud'])
    _address = conf['address']
    if _cloud:
        cloud = 'True'
        _server = _address.split('/')[-1]
        address = _address[:-len(_server)]
        ssl = True
    else:
        cloud = 'False'
        address = _address
        port = conf['port']
        ssl = conf['ssl']
        _server = instance
        gateway = conf['gateway']
        namespace = conf['namespace']
    if _cloud:
        _config = {
            'cloud': cloud,
            'address': address,
            'server': _server
        }
    else:
        _config = {
            'cloud': 'False',
            'address': address,
            'port': port,
            'ssl': ssl,
            'namespace': namespace,
            'gateway': gateway,
            'server': instance
        }
    return _config


def str_to_bool(response: str) -> bool:
    return response.lower() in ['y', 'yes', 't', 'true', '1', 'on']
