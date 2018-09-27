
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


async def hello(url):
    response = await client.get(url)
