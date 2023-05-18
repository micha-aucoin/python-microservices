from pydantic import BaseSettings


class Settings(BaseSettings):
    rabbitmq_host: str
    mp3_queue: str

    email_address: str
    email_password: str
