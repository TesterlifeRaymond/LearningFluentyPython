# -*- coding: utf-8 -*-
"""
    LearningFluentyPython.__init__
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    DESCRIPTION

    :copyright: (c) 2018 by  Raymond.
    :last modified by 2018-09-11 17:34:38
"""

import asyncio
import aiohttp
import time

start = time.time()
session = aiohttp.ClientSession()


async def get(url):
    response = await session.get(url)
    result = await response.text()
    session.close()
    return result


async def request(num):
    url = 'http://www.gzgtzy.gov.cn/zwgk/xxgkml/xxgk_list_{}.html'.format(num)
    print('Waiting for', url)
    return await get(url)


tasks = [asyncio.ensure_future(request(i)) for i in range(10)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('Cost time:', end - start)
