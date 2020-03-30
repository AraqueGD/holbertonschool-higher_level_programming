#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    sql = session.query(State).filter_by(id=2).first()
    sql.name = 'New Mexico'
    session.commit()

    sql = session.query(State).filter_by(name="Louisiana").first()
    print("{}".format(sql.id))
    session.close()
