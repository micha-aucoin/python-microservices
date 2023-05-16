from pydantic import BaseSettings


class Settings(BaseSettings):
    # Base
    api_v1_prefix: str
    debug: bool
    project_name: str
    version: str
    description: str

    # mongo
    mongo_connection_str: str

    # rabbitmq
    rabbitmq_host: str

    # Auth
    auth_host: str
    auth_api_v1_prefix: str
