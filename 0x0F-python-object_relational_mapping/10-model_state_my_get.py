#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    aux = 0
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    name_db = argv[4]
    session = Session(engine)

    for state in session.query(State).filter(State.name == name_db):
        print("{}".format(state.id))
        aux = 1
    if (aux == 0):
        print("Not Found")
    session.close()
