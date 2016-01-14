import os
import json
import requests

from settings import ROOT_DIR
from crawler.wrappers.exceptions import TrulioException


class TrulioAPI:

    def __init__(self):
        with open(os.path.join(ROOT_DIR, 'crawler/wrappers/trulio_key.txt')) as f:
            self.api_key = f.read()


    def base_api_call(self):
        return self.__class__.__name__










if __name__ == '__main__':
    raise TrulioException('This file should not be called directly, terminating ... ')
