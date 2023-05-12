from pydantic import BaseSettings


class Config(BaseSettings):
    KAFKA_TOPIC: str = "mytopic"
    KAFKA_HOST: str = "localhost"
    KAFKA_PORT: int = 9092
    REDIS_DB_NUM: int = 0
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379


config = Config()
