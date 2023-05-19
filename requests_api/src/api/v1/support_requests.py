from datetime import datetime
from typing import Annotated
from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import ORJSONResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from aiokafka import AIOKafkaProducer
from redis import Redis

from api.v1.schemas import ModelIn
from db.kafka import get_kafka_producer
from db.redis_storage import get_redis_storage
from config.settings import config
from models.payload import Payload

router = APIRouter()

bearer_token = HTTPBearer()


def get_client_id(token: Annotated[HTTPAuthorizationCredentials, Depends(bearer_token)],
                  token_storage_service: Annotated[Redis, Depends(get_redis_storage)],
                  ):
    return token_storage_service.get(token.credentials)


@router.post("/push", summary="Push request to kafka")
async def push_request(body: ModelIn,
                       kafka_producer: Annotated[AIOKafkaProducer, Depends(get_kafka_producer)],
                       user_id: Annotated[str, Depends(get_client_id)]):
    if not user_id:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED)
    await kafka_producer.send_and_wait(
        value=Payload(user_id=user_id, text=body.text, timestamp=datetime.now()).json().encode(),
        topic=config.KAFKA_TOPIC, key=user_id)
    print("hey")
    return ORJSONResponse({})
