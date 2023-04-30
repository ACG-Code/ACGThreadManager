from configparser import ConfigParser
from baseSettings import application_path, APP_NAME
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


def retrieve_tm1_config(instance: str) -> dict:
    """
    Create dictionary to use for connecting to TM1PyService
    :param instance: Config.ini section
    :return: dictionary
    """
    base_url = None
    address = None
    port = None
    gateway = None
    namespace = None
    ssl = False
    _config = {}
    config = ConfigParser()
    config.read(FILE)
    conf = dict(config.items(instance))
    _cloud = str_to_bool(conf['cloud'])
    if _cloud:
        base_url = conf.get("address")
    else:
        address = conf.get("address")
        port = conf.get("port")
        ssl = conf.get("ssl")
        gateway = conf.get("gateway")
        if gateway == '':
            gateway = None
        namespace = conf.get("namespace")
        if namespace == '':
            namespace = None
    if _cloud:
        _config = {
            'base_url': base_url,
            'namespace': 'LDAP',
            'ssl': True,
            'verify': True,
            'async_requests_mode': True,
            'session_context': APP_NAME
        }
    else:
        _config = {
            'address': address,
            'port': port,
            'ssl': ssl,
            'namespace': namespace,
            'gateway': gateway,
            'session_context': APP_NAME
        }
    return _config


def get_sections() -> list:
    sec_list = ['']
    config = ConfigParser()
    file = os.path.join(application_path, 'config.ini')
    config.read(file)
    for section in config.sections():
        sec_list.append(section)
    return sec_list
