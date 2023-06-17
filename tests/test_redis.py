import unittest
from config import Configuration
import subprocess

class TestRedis(unittest.TestCase):
    import redis
    config = Configuration()
    redis_url = config.REDIS_URL
    r = redis.from_url(redis_url)
    try:
        r.ping()
    except Exception:
        try:
            subprocess.Popen("systemctl restart redis-server.service", shell=True)
        except Exception:
            subprocess.Popen("service redis-server start", shell=True)

