#!/usr/bin/python3
"""
lists all State objects, and City objects, in the database hbtn_0e_101_usa
"""
import sys
import os
import sqlalchemy
from sqlalchemy import *
import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    for i in session.query(State):
        print("{}: {}".format(i.id, i.name))
        st = i.id
        for j in session.query(City).filter(City.state_id == st):
            print("    {}: {}".format(j.id, j.name))
    session.commit()
    session.close()
