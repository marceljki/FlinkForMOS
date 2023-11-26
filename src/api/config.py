import configparser


class Config:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('api_keys.ini')

    def get(self, name: str) -> str:
        return self.config.get('API_KEYS', name)
