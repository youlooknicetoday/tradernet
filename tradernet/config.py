import configparser
from pathlib import Path


def read_config(path: Path = None):
    config = configparser.ConfigParser()
    if path and Path.exists(path):
        config.read(path)
    elif not path and (path := Path.joinpath(Path.cwd(), 'api.ini')).exists():
        config.read(path)
    else:
        raise FileNotFoundError
    return config['tradernet'].values()
