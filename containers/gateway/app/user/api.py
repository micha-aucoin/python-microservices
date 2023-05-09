from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi import status as http_status

from app.user.dependencies import get_current_active_user
from app.user.models import UserRead

router = APIRouter()


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
