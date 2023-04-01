import sys
import logging

from .constants import FILE_NOT_FOUND

class FileException(Exception):
    def __init__(self, file_path):
        self.file_path = file_path
        logging.error(f'{FILE_NOT_FOUND}: {self.file_path}')
        sys.exit(1)
