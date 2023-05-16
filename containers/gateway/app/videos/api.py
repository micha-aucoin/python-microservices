from typing import Annotated

import gridfs
import pika
from app import settings
from app.core.models import TokenData
from app.videos.storage import upload
from app.videos.validate import get_token
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from pymongo import MongoClient

router = APIRouter()


pymongo_client = MongoClient(settings.mongo_connection_str)
pymongo_db = pymongo_client.videos


fs_videos = gridfs.GridFSBucket(pymongo_db)

connection = pika.BlockingConnection(pika.ConnectionParameters(settings.rabbitmq_host))
channel = connection.channel()


@router.post("/upload")
async def upload_file(
    authorization: Annotated[TokenData, Depends(get_token)],
    file: UploadFile = File(...),
):
    if not authorization:
        raise HTTPException(status_code=401, detail="Not authorized")

    else:
        upload(file, fs_videos, channel, authorization)

        return {"detail": "Success!"}


@router.get("/download")
async def download_file():
    pass
