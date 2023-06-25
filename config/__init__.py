import os
from dotenv import dotenv_values


class Config:
    def __init__(self, file_path=None):
        print(file_path)
        if file_path is not None:
            self._config = self.load_config_from_file(file_path)
        else:
            self._config = {}

    @staticmethod
    def load_config_from_file(file_path):
        _, file_extension = os.path.splitext(file_path)

        if file_path == '.env':
            config = dotenv_values(file_path)
        else:
            raise ValueError(
                'Unsupported configuration file format: {}'.format(file_extension))

        return config

    def get(self, key, default=None):
        return self._config.get(key, default)


config = Config(file_path=".env")
