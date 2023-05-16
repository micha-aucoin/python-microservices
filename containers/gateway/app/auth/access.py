import httpx
from app import settings
from fastapi import HTTPException, status


async def token(
    username: str,
    password: str,
):
    url = f"http://{settings.auth_host}{settings.auth_api_v1_prefix}/auth/token"
    data = {"username": username, "password": password}

    async with httpx.AsyncClient() as client:
        response = await client.post(
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
