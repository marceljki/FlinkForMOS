import configparser
import os


class Config:

    def __init__(self):
        self.config = configparser.ConfigParser()
        filename = '../api_keys.ini'
        if os.path.isfile(filename):
            self.config.read(filename)
        else:
            print("File \"%s\" does not exist" % filename)

    def get(self, name: str) -> str:
        return self.config.get('API_KEYS', name)
