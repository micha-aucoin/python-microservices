from typing import Annotated

import httpx
from app import settings
from app.user.models import UserRead
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f".{settings.api_v1_prefix}/auth/token")


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    url = f"http://{settings.auth_host}{settings.auth_api_v1_prefix}/users"
    headers = {"Authorization": f"Bearer {token}"}

    async with httpx.AsyncClient() as client:
        response = await client.get(
            url=url,
            headers=headers,
        )

    if response.status_code == status.HTTP_200_OK:
        user = UserRead(**response.json())
        return user

    else:
        raise credentials_exception


async def get_current_active_user(
    current_user: Annotated[UserRead, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
