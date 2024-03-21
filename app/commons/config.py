from os import path, environ, getenv
from enum import Enum
from typing_extensions import Unpack
from pydantic import BaseModel, ConfigDict
from abc import ABC, abstractclassmethod
from typing import Any

subclass_registry = {}


class ModifiedBaseModel(BaseModel):
    def __init_subclass__(cls, is_abstract: bool = False, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)
        if not is_abstract:
            subclass_registry[cls.__name__s] = cls


class Config(ModifiedBaseModel, ABC, is_abstract=True):
    '''
    config
    '''

    BASEDIR: str = path.dirname(path.dirname(path.dirname(__file__)))
    DEBUG: bool = True

    @abstractclassmethod
    def get_db_url(self) -> None | str:
        raise NotImplementedError
    

class ProdConfig(Config):
    DEBUG: bool = False

    def get_db_url(self) -> None | str:
        return None
    

class LocalConfig(Config):
    DEBUG: bool = True

    def get_db_url(self) -> None | str:
        USERNAME = 'root'
        PASSWORD = 'admin'
        HOST = '192.168.0.100'
        PORT = 3306
        DBNAME = 'example'
        return f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}'
    

def conf():
    '''
    get config
    '''

    match environ.get("API_ENV", "local"):
        case "prod":
            return ProdConfig()
        case "local":
            return LocalConfig()

