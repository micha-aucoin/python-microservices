from pydantic import BaseSettings


class Settings(BaseSettings):
    mongo_connection_str: str
    rabbitmq_host: str
    video_queue: str
    mp3_queue: str
