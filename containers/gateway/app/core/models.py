from datetime import datetime

from pydantic import BaseModel


class HealthCheck(BaseModel):
    name: str
    version: str
    description: str
