import configparser
from dataclasses import dataclass, asdict


@dataclass
class Config:
    apikey: str
    secret: str

    @property
    def representation(self):
        return asdict(self)


def load_config(path):
    config = configparser.ConfigParser()
    config.read(path)
    return Config(**config['tradernet'])

