import requests
from fastapi import HTTPException, status

from app import settings


async def authenticate_user(
    username: str,
    password: str,
):
    url = f"http://{settings.auth_host}{settings.api_v1_prefix}/auth/token"
    data = {
        "username": username,
        "password": password,
    }

    response = requests.post(
        url=url,
        data=data,
    )

    if response.status_code == status.HTTP_200_OK:
        return response.json()
    else:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.text,
        )
