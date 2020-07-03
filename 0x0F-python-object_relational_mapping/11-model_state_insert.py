#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa using sqlalchemy
"""
import sys
import sqlalchemy
from sqlalchemy import *
import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy import MetaData, Table
from model_state import Base, State
from sqlalchemy.sql import table, column, select, update, insert
from sqlalchemy import update

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = scoped_session(sessionmaker(bind=engine))
    session = Session()
    addition = State(name='Louisiana')
    session.add(addition)
    session.commit()
    print("{}".format(addition.id))
    session.close()
