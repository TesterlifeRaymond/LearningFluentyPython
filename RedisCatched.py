
# -*- coding: utf-8 -*-
"""
    LearningFluentyPython.RedisCatched
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    redis client catched demo

    :copyright: (c) 2018 by  Raymond.
    :last modified by 2018-08-16 14:11:46
"""

import redis
import time
from datetime import datetime, timedelta


def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton


@Singleton
class RedisClient:
    __redis = redis.Redis()
    __catched = {}

    def __getattr__(self, key):
        func = key in dir(self)
        if func:
            return dir(self).pop(key)
        return getattr(self.__redis, key)

    def __getitem__(self, key):
        if key in self.__catched:
            value, ex = self.__catched[key]
            now = datetime.now()
            if (now < ex):
                return value
        searched = self.__redis.get(key)
        self.__catched.update({key: searched})
        return searched

    def __setitem__(self, key, value):
        value, ex = value
        self.__redis.set(key, value, ex)
        expire = datetime.now() + timedelta(seconds=ex)
        self.__catched[key] = [value, expire]
        print("insert {} doc : {}, expire time : {}".format(key, value, ex))

    def __delitem__(self, key):
        self.__redis.delete(key)
        self.__catched.pop(key)

    def set(self, key, value, ex=14400):
        value = (value, ex)
        self.__setitem__(key, value)

    def get(self, key):
        return self.__getitem__(key)

    def delete(self, key):
        print("clear {} in self.__catched. ".format(key))
        self.__delitem__(key)


if __name__ == "__main__":
    client = RedisClient()
    # print(client.info())
    # print(client.get(b"ec972ac103cc72e20dd3fd79768c80c0"))
    client.set("123", 123, ex=3)
    print(client.get("123"))
    client.delete("123")
    print(client.get("123"))
