#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa using sqlalchemy
"""
import sys
import os
from sqlalchemy import *
import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy import MetaData, Table

if __name__ == '__main__':
    Base = declarative_base()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    metadata = MetaData()       # instatiate intense of MetaData
    states = Table('states', metadata, autoload=True, autoload_with=engine)
    Base.metadata.create_all(engine)
    session = scoped_session(sessionmaker(bind=engine))
    for state in session.query(states).order_by(states).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
