# coding: utf-8
import redis
import json
from django.conf import settings


class Resource(object):

    def __init__(self):
        self._config()
        self._client = self.connect()

    def _config(self):
        self._host = settings.REDIS_DB['host']
        self._port = settings.REDIS_DB['port']
        self._pass = settings.REDIS_DB['pass']
        self._db = settings.REDIS_DB['db']

    def connect(self):
        return redis.StrictRedis(host=self._host, port=self._port, db=self._db,
                                 password=self._pass)

    def get(self, key):
        result = self._client.get(key)
        if result:
            try:
                result = json.loads(result)
            except ValueError:
                pass
        return result

    def set(self, key, value):
        try:
            value = json.dumps(value)
        except ValueError:
            pass
        return self._client.set(key, value)

    def zadd(self, key, **kwargs):
        return self._client.zadd(key, **kwargs)

    def zrange(self, key, reverse=True):
        result = self._client.zrange(key, 0, -1, withscores=False)
        if reverse:
            return reversed(result)
        return result
