from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi import status as http_status
from fastapi.security import OAuth2PasswordRequestForm

from app.auth_srv.dependencies import authenticate_user
from app.auth_srv.models import Token

router = APIRouter()


@router.post(
    "/token",
    response_model=Token,
    status_code=http_status.HTTP_200_OK,
)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
):
    token = await authenticate_user(
        username=form_data.username,
        password=form_data.password,
    )
    if not token:
        raise HTTPException(
            status_code=http_status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token
