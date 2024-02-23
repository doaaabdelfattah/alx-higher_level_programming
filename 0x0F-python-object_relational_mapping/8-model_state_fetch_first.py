#!/usr/bin/python3
"""Start link class to table in database
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker, scoped_session
import sys
from sqlalchemy import create_engine


if __name__ == "__main__":

    host = 'localhost'
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    url = f'mysql+mysqldb://{user}:{passwd}@{host}/{db}'
    engine = create_engine(url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    row = session.query(State).order_by(State.id).first()
    print("{}: {}".format(row.id, row.name))
