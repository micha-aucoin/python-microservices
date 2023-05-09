from pydantic import BaseModel

from app.user.examples import ex_user_create, ex_user_patch, ex_user_read


class UserBase(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserRead(UserBase):
    class Config:
        schema_extra = {"example": ex_user_read}


class UserCreate(UserBase):
    password: str

    class Config:
        schema_extra = {"example": ex_user_create}


class UserPatch(UserBase):
    username: str | None = None

    class Config:
        schema_extra = {"example": ex_user_patch}
