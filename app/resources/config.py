from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_name: str
    database_password: str
    database_username: str
    jwt_secret_key: str
    first_login: str
    first_password: str
    first_email: str
    environment: str

    class Config:
        env_file = ".env"


settings = Settings()