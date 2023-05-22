from __future__ import print_function
import logging
from entities.Credentials import MyCredentials
class ControllerGoogle:
    def __init__(self):
        try:
            self.credential = MyCredentials.get_credentials()
        except Exception as e:
            logging.error(f'{" "* 3} Erro: {e}')