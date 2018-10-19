
# -*- coding: utf-8 -*-
"""
    Vibora.hello_world
    ~~~~~~~~~~~~~~~~~~

    vibora demo

    :copyright: (c) 2018 by  Raymond.
    :last modified by 2018-09-27 15:25:34
"""

import asyncio
from vibora import client
from lxml import etree


async def parse(html, xpath="//title/text()"):
    element = etree.HTML(html).xpath(xpath)
    return element


async def hello_world():
    response = await client.get('http://testerlife.com/')
    print(f'Content: {response.content}')
    print(f'Status code: {response.status_code}')
    title = await parse(response.content.decode())
    print(title)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello_world())
