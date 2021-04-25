from pydantic import BaseSettings


class CommonSettings(BaseSettings):
    APP_NAME: str = "FARM Starter"
    DEBUG_MODE: bool = False


class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000


class DatabaseSettings(BaseSettings):
    DB_URL: str = "mongodb+srv://amit:amit@clustermumbai.56wzg.mongodb.net/To_Do_App?retryWrites=true&w=majority"
    DB_NAME: str = "To_Do_App"


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass


settings = Settings()