from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:admin1234@localhost:5432/Escuela_Fastapi"

    class Config:
        env_file = ".env"

settings = Settings()
