#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    name_db = argv[4]
    Session = sessionmaker(bind=engine)
    session = Session()

    sql = session.query(State).filter(State.name == name_db)
    states = sql.all()

    if states:
        for state in states:
            print(state.id)
    else:
        print("Not found")
