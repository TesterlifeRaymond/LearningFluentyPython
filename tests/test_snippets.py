# -*- coding: utf-8 -*-
"""
    LearningFluentyPython.test_snippets
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    ThreadPoolExecutor

    :copyright: (c) 2018 by  Raymond.
    :last modified by 2018-07-09 17:20:19
"""

import time
import random
from concurrent.futures import ThreadPoolExecutor


def get_max_num(max_num):
    print(f"{max_num} is running")
    return max_num


if __name__ == "__main__":
    max_num = (55, 32, 66, 7, 2)
    thread = ThreadPoolExecutor(max_workers=3)

    for item in max_num:
        result = thread.submit(get_max_num, item)
        print(result)
