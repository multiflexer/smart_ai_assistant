from redis import Redis

redis_storage: Redis | None = None


def get_redis_storage():
    return redis_storage
