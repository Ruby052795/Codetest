import requests
import configparser
import os


current_dir = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(current_dir, '../../config/setting.ini')

config = configparser.ConfigParser()
config.read(config_path)
BASE_URL = config.get('API','REST_BASE_URL')
CANDLESTICK_ENDPOINT = config.get('API','GET_CANDLESTICK')


class PublicApiClient:
    def __init__(self, ):
        self.url_base = f"https://{BASE_URL}/{CANDLESTICK_ENDPOINT}"
        self.response = None

    def get_candlestick(self, params):
        # remove empty params to ensure only
        clean_params = {k: v for k, v in params.items() if v is not None}
        self.response = requests.get(self.url_base, params=clean_params, timeout=10)
        return self.response
