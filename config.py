"""The file with the project settings"""
from pydantic import IPvAnyAddress, PostgresDsn
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
        The class with the project settings

        Args:
            host: IP address for connection
            port: the endpoint for transferring data between users
            postgres_url: db connection string
    """
    host: IPvAnyAddress = '127.0.0.1'
    port: int = 8000
    postgres_url: PostgresDsn

    class Config():
        """F class with a settings file"""
        env_file = '.env'

Config = Settings()
