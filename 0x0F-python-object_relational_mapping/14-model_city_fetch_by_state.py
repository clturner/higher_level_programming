#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa from joined tables:
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
    for i in session.query(City).join(State):
        print("{}: ({}) {}".format(i.state.name, i.id, i.name))
    session.commit()
    session.close()
