"""
@Version: 1.0
@Project: FluentyPython
@Author: Raymond
@Data: 2018/4/11 下午3:33
@File: MakeMetaClass.py
@License: MIT
"""
from lxml import etree
from MetaClass import LoggerMeta
import asyncio
from asyncio import get_event_loop
from aiohttp import ClientSession
import async_timeout

loop = get_event_loop()
session = ClientSession(loop=loop)


class Crawl(metaclass=LoggerMeta):
    # TODO: BugFix
    def __init__(self):
        self.response = None
        self.session = session
        self.html = None
        self.etree = etree
        self._xpath = None

    async def fetch(self, url):
        async with async_timeout.timeout(10):
            async with self.session.get(url) as resp:
                return resp


async def main(crawl, url):
    result = await crawl.fetch(url)
    crawl.logger.info("[ RESPONSE URL ]: {}".format(result.url))
    return result


if __name__ == '__main__':
    crawl = Crawl()
    urls = [
        "http://testerlife.com",
        "http://163.com",
        "http://httpbin.org/ip"
    ]
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(main(crawl, url))
        tasks.append(task)
    result = loop.run_until_complete(asyncio.wait(tasks))
    session.close()
