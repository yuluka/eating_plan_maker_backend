from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Configuration settings for the application.
    """

    CONTEXT_PATH: str

    # FOR DATABASE CONNECTION
    DB_NAME: str
    DB_HOST: str
    DB_PORT: int = 5432
    DB_USER: str
    DB_PASSWORD: str

    @property
    def db_url(self) -> str:
        """
        Retrieve the DB connection url.

        :return: The DB connection url.
        :rtype: str
        """

        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()
