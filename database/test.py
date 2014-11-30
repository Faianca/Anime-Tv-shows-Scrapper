from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from db import Episodes, Series, Base
 
engine = create_engine('sqlite:///faianca_entertainment.db')

Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)

session = DBSession()
 
# Insert a Person in the person table
new_serie = Series(name='test episode', release_date="2014")
session.add(new_serie)
session.commit()
 
# Insert an Address in the address table
new_episode = Episodes(name='dasdad', serie=new_serie)
session.add(new_episode)
session.commit()