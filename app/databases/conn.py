from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class DBConnector:
    
    def __init__(self, app:FastAPI=None, **kwargs) -> None:
        
        self._engine = None
        self._session = None

        if app is not None:
            self.initialize(app=app, **kwargs)

    def initialize(self, app:FastAPI, **kwargs) -> None:

        pool_recycle = 900
        echo = True

        self._engine = create_engine(
            kwargs.get("DB_URL"),
            echo=echo,
            pool_recycle=pool_recycle,
            pool_pre_ping=True
        )
        self._session = sessionmaker(autocommit=False, autoflush=False, bind=self._engine)

        @app.on_event("startup")
        def startup():
            self._engine.connect()


        @app.on_event("shutdown")
        def shutdown():
            self._session.close_all()
            self._engine.dispose()

    def get_db(self):
        
        if self._session in None:
            raise Exception("colled initialize")
        
        db_session = None

        try:
            db_session = self._session()
            yield db_session
        finally:
            db_session.close()

    @property
    def session(self):
        return self.get_db
    
    @property
    def engine(self):
        return self._engine
    
db_conn = DBConnector()