"""
@Version: 1.0
@Project: FluentyPython
@Author: Raymond
@Data: 2018/1/25 下午1:27
@File: file_handler.py
@License: MIT
"""
import click
import logging
logging.basicConfig(filename='catelina.log',
                    format='%(asctime)s -%(name)s-%(levelname)s-%(module)s:%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class FileHandler:
    """
        FileHandler 
        基于Python __enter__ __exit__ 对上下文进行管理,
        通过read及write方法支持file文件同时读写的操作行为
    """

    def __init__(self, filename: str, mod: str = 'r', encoding: str ="utf-8"):
        """
            初始化类属性
        @params: filename
        @params: mod
        @params: encoding
        """
        self.filename = filename
        if mod not in ['r', 'w']:
            encoding = None
        self.file = open(filename, mod, encoding=encoding)
        self.mod = mod

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            logger.info(f"Raise {exc_type}: {exc_val}")
        else:
            self.file.close()
            logger.info(f"close file : {self.file} done ..")

    def read(self):
        return self.file.readlines()

    def write(self, msg, mod='a'):
        with FileHandler(self.filename, mod=mod) as wfile:
            wfile.file.writelines(msg)


@click.command()
@click.option("--file", help="specify the path to a file", prompt="filename")
@click.option("--mod", help="read or write", prompt="file mod", default="r")
def run(file, mod):
    if mod not in ('r', 'a', 'rb'):
        msg = "write msg ..\n"
        with FileHandler(file, mod) as obj:
            obj.write([msg])
            print(msg.strip() + "is done")
    else:
        with FileHandler(file, mod) as obj:
            print(obj.read())


if __name__ == '__main__':
    while 1:
        try:
            run()
        except KeyboardInterrupt:
            break
