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
from model_state import Base, State

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = scoped_session(sessionmaker(bind=engine))
    session = Session()
    state = session.query(State.id, State.name).first()
    metadata = MetaData()
    Base.metadata.create_all(engine)
    try:
        print("{}: {}".format(state[0], state[1]))
    except:
        print("Nothing")
    session.close()
