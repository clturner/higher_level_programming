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
    flag = 0
    state_passed_in = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    metadata = MetaData()       # instatiate intense of MetaData
    states = Table('states', metadata, autoload=True, autoload_with=engine)
    Session = scoped_session(sessionmaker(bind=engine))
    session = Session()
    for state in session.query(State).filter_by(name=state_passed_in):
        if state.name == sys.argv[4]:
            print(state.id)
            flag = 1
    if flag == 0:
        print("Not found")
    session.close()
