from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer

class Base(object):

    __tabel_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)


Base = declarative_base(cls=Base)