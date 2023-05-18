import json

import pika
from app.core.models import TokenData
from fastapi import HTTPException, UploadFile


def upload(f: UploadFile, fs, channel, token_data: TokenData):
    try:
        fid = fs.put(f.file)
    except Exception as err:
        print(err)
        raise HTTPException(status_code=500, detail="Internal server error")

    message = {
        "video_fid": str(fid),
        "mp3_fid": None,
        "email": token_data.email,
    }

    try:
        channel.basic_publish(
            exchange="",
            routing_key="video",
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
    except Exception as err:
        print(err)
        fs.delete(fid)
        raise HTTPException(status_code=500, detail="Internal server error")
