"""
@Version: 1.0
@Project: FluentyPython
@Author: Raymond
@Data: 2018/1/25 下午1:27
@File: file_handler.py
@License: MIT
"""
import sys
import logging
from io import StringIO
logging.basicConfig(format='%(asctime)s -%(name)s-%(levelname)s-%(module)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=logging.DEBUG,
                    stream=sys.stderr,
                    )
logger = logging.getLogger(__name__)


class FileHandler:
    def __init__(self, msg: str):
        self.file = StringIO()
        self.file.write(msg)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            logger.info(f"Raise {exc_type}: {exc_val}")
        else:
            logger.info(f"close file : {self.file} done ..")

    def read(self):
        return repr(self.file.getvalue())

    def write(self, msg):
        self.file.write('\n' + msg)


if __name__ == '__main__':
    with FileHandler("Hello") as file:
        data = file.read()
        logger.info(data)
        file.write("6666")
        logger.info(file.read())
