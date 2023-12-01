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
        if not os.path.exists(self.get_out_path()):
            os.makedirs(self.get_out_path())

    def get(self, name: str) -> str:
        return self.config.get('API_KEYS', name)

    def get_out_path(self):
        return self.config.get("PATHS", "OUT_PATH")

