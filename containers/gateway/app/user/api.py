from typing import Annotated

import httpx
from app import settings
from app.user.dependencies import get_current_active_user
from app.user.models import UserCreate, UserRead
from fastapi import APIRouter, Depends, HTTPException
from fastapi import status as http_status

router = APIRouter()


@router.post(
    "",
    response_model=UserRead,
    status_code=http_status.HTTP_201_CREATED,
)
async def create_user(data: UserCreate):
    url = f"http://{settings.auth_host}{settings.auth_api_v1_prefix}/users"
    data = data.json()

    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=url,
            data=data,
        )
    if response.status_code == http_status.HTTP_200_OK:
        user = UserRead(**response.json())
        return user

    else:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.json(),
        )


@router.get(
    "",
    response_model=UserRead,
    status_code=http_status.HTTP_200_OK,
)
async def get_user(current_user: Annotated[UserRead, Depends(get_current_active_user)]):
    return current_user


# @router.patch(
#     "",
#     response_model=UserRead,
#     status_code=http_status.HTTP_200_OK,
# )
# async def patch_user(
#     current_user: Annotated[UserRead, Depends(get_current_active_user)],
#     data: UserPatch,
#     users: UserCRUD = Depends(get_user_crud),
# ):
#     try:
#         user = await users.patch(username=current_user.username, data=data)
#     except IntegrityError as e:
#         raise HTTPException(
#             status_code=http_status.HTTP_400_BAD_REQUEST,
#             detail="The username or email is already in use.",
#         ) from e

#     return user


# @router.delete(
#     "",
#     response_model=StatusMessage,
#     status_code=http_status.HTTP_200_OK,
# )
# async def delete_user(
#     current_user: Annotated[UserRead, Depends(get_current_active_user)],
#     users: UserCRUD = Depends(get_user_crud),
# ):
#     status = await users.delete(username=current_user.username)

#     return {
#         "status": status,
#         "message": f"The user, {current_user.username} has been deleted!",
#     }
