import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from aiokafka import AIOKafkaProducer
from redis import Redis

from api.v1 import support_requests
from config.settings import config
from db import kafka, redis_storage

app = FastAPI(
    title='Support requests pusher',
    docs_url='/api/docs',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)


@app.on_event('startup')
async def startup():
    kafka.kafka_producer = AIOKafkaProducer(bootstrap_servers=[
        f"{config.KAFKA_HOST}:{config.KAFKA_PORT}"
    ])
    await kafka.kafka_producer.start()
    redis_storage.redis_storage = Redis(host=config.REDIS_HOST,
                                        port=config.REDIS_PORT,
                                        db=config.REDIS_DB_NUM)


@app.on_event('shutdown')
async def shutdown():
    await kafka.kafka_producer.stop()


app.include_router(support_requests.router, prefix='/api/v1/requests', tags=['Support requests'])

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
    )
