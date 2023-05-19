from pydantic import BaseSettings


class Config(BaseSettings):
    KAFKA_OUTPUT_TOPIC: str = "outtopic"
    KAFKA_INPUT_TOPIC: str = "mytopic"
    KAFKA_INPUT_CONSUMER_GROUP: int = 1
    KAFKA_HOST: str = "localhost"
    KAFKA_PORT: int = 9092


config = Config()
