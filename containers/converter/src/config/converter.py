from pydantic import BaseSettings


class Settings(BaseSettings):
    db_connection_str: str

    queue_connection_str: str
