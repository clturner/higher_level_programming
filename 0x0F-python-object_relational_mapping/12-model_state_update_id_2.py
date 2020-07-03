#!/usr/bin/python3
"""
changes the name of a State object from the database hbtn_0e_6_usa
"""
import sys
import os
import sqlalchemy
from sqlalchemy import *
import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    db_change = session.query(State).filter_by(id=2).first()
    db_change.name = "New Mexico"
    session.commit()
    session.close()
