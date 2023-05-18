from datetime import datetime

from pydantic import BaseModel


class HealthCheck(BaseModel):
    name: str
    version: str
    description: str


class StatusMessage(BaseModel):
    status: bool
    message: str


class TokenData(BaseModel):
    email: str | None = None
