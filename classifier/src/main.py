import asyncio

from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
from pydantic import ValidationError

from config.settings import config
from models.payload import Payload, PayloadOut
from service.models import get_request_classifier_service


async def main():
    model = get_request_classifier_service()
    kafka_producer = AIOKafkaProducer(bootstrap_servers=f"{config.KAFKA_HOST}:{config.KAFKA_PORT}")
    consumer = AIOKafkaConsumer(
        config.KAFKA_INPUT_TOPIC,
        group_id=config.KAFKA_INPUT_CONSUMER_GROUP,
        bootstrap_servers=f"{config.KAFKA_HOST}:{config.KAFKA_PORT}",
        auto_offset_reset='earliest',
        enable_auto_commit=False)
    await consumer.start()
    try:
        while True:
            msg = await consumer.getone()
            print(f"Message from partition [{msg.partition}]: {msg.value}")
            try:
                payload = Payload.parse_raw(msg.value)
            except ValidationError:
                continue
            result = model.compute(payload.text)
            payload_out = PayloadOut(result_class=result, **payload.dict())
            await kafka_producer.send_and_wait(value=payload_out.json().encode(),
                                               topic=config.KAFKA_OUTPUT_TOPIC,
                                               key=payload_out.user_id)
            await consumer.commit()
    finally:
        await consumer.stop()
        await kafka_producer.stop()


if __name__ == '__main__':
    asyncio.run(main())
