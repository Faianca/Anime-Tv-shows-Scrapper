from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Series(Base):
    __tablename__ = 'series'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    release_date = Column(String(250), nullable=True)
    episodes = relationship("Episodes", backref="series")


class Episodes(Base):
    __tablename__ = 'episodes'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    serie_id = Column(Integer, ForeignKey('series.id'))
    serie = relationship(Series)

engine = create_engine('sqlite:///faianca_entertainment.db')
Base.metadata.create_all(engine)