from typing import Annotated

import gridfs
import pika
from bson.objectid import ObjectId
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from fastapi.responses import FileResponse
from pymongo import MongoClient

from app import settings
from app.core.models import TokenData
from app.videos.storage import upload
from app.videos.validate import get_token

router = APIRouter()


pymongo_client = MongoClient(settings.mongo_connection_str)

pymongo_videos = pymongo_client.videos
pymongo_mp3s = pymongo_client.mp3s

fs_videos = gridfs.GridFS(pymongo_videos)
fs_mp3s = gridfs.GridFS(pymongo_mp3s)

connection = pika.BlockingConnection(pika.ConnectionParameters(settings.rabbitmq_host))
channel = connection.channel()


@router.post("/upload")
async def upload_file(
    token_data: Annotated[TokenData, Depends(get_token)],
    file: UploadFile = File(...),
):
    upload(file, fs_videos, channel, token_data)

    return {"detail": "Success!"}


@router.get("/download/{fid}")
async def download_file(
    token_data: Annotated[TokenData, Depends(get_token)],
    fid: str,
):
    if not token_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authorized",
        )

    try:
        file_id = ObjectId(fid)
        if not fs_mp3s.exists(file_id):
            raise HTTPException(status_code=404, detail="File not found")

        grid_out = fs_mp3s.get(file_id)

        # create a temp file and write the content
        with open(f"{fid}.mp3", "wb") as f:
            f.write(grid_out.read())

        return FileResponse(
            f"{fid}.mp3", filename=f"{fid}.mp3", media_type="audio/mpeg"
        )
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal server error")
