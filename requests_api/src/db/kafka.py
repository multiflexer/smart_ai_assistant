from aiokafka import AIOKafkaProducer

kafka_producer: AIOKafkaProducer | None = None


def get_kafka_producer():
    return kafka_producer
