from typing import Annotated

import httpx
from app import settings
from app.core.models import TokenData
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f".{settings.api_v1_prefix}/auth/token")


async def get_token(
    token: Annotated[str, Depends(oauth2_scheme)],
):
    url = f"http://{settings.auth_host}{settings.auth_api_v1_prefix}/auth/validate"
    headers = {"Authorization": f"Bearer {token}"}

    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=url,
            headers=headers,
        )
    if response.status_code == status.HTTP_200_OK:
        return TokenData(**response.json())
    else:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.text,
        )
