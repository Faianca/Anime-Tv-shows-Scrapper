from db import Episodes, Series, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///faianca_entertainment.db')
Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

# Return the first Person from all Persons in the database
serie = session.query(Series).first()
episodes = session.query(Episodes).filter(Episodes.serie == serie).all()

for episode in episodes:
    print episode.name