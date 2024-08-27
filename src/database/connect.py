import redis
from src.core.config import settings


##################
# Redis Connection
##################


def init_redis_pool():
    redis_host = settings.REDIS_HOST
    redis_port = settings.REDIS_PORT
    redis_pass = settings.REDIS_PASSWORD
    pool = redis.ConnectionPool(
        host=redis_host, port=redis_port, password=redis_pass, db=0
    )
    return pool


redis_client = redis.Redis(connection_pool=init_redis_pool())
