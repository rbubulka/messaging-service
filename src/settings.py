"""Settings that will be used throughout the application."""
import logging
import os
import sys
from typing import Any, Dict, List, Tuple
from sqlalchemy import URL
from pydantic import PostgresDsn



class AppSettings():
    """Bundle all app settings."""
    app_env: str = os.getenv("APP_ENV")

    # FastAPI App settings
    debug: bool = False
    docs_url: str = "/docs"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    allowed_hosts: List[str] = ["*"]

    title: str = os.getenv("APP_TITLE")
    version: str = os.getenv("APP_VERSION")
    description: str = os.getenv("APP_DESCRIPTION")
    api_prefix: str = "/api"

    # database settings
    db_user: str = os.environ['DB_USER']
    db_password: str = os.environ['DB_PASSWORD']
    db_host: str = os.environ['DB_HOST']
    db_port: int = os.environ['DB_PORT']
    db_name: str = os.environ['DB_NAME']


    # logging
    logging_level: int = logging.DEBUG
    loggers: Tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")


    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "openapi_prefix": self.openapi_prefix,
            "openapi_url": self.openapi_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "version": self.version,
            "description": self.description,
        }
    
    @property
    def database_settings(self) -> Dict[str, Any]:
        return {
            "db_user": self.db_user,
            "db_password": self.db_password,
            "db_host": self.db_host,
            "db_port": self.db_port,
            "db_name": self.db_name,
        }
    
    @property
    def database_url(self) -> PostgresDsn:
        return URL.create('postgresql+asyncpg',
                          username = self.database_settings.get("db_user"),
                          password = self.database_settings.get("db_password"),
                          host = self.database_settings.get("db_host"),
                          port= self.database_settings.get("db_port"),
                          database = self.database_settings.get("db_name"))
