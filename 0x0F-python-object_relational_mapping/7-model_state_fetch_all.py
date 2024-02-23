#!/usr/bin/python3
"""Start link class to table in database 
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker, scoped_session
import sys
from sqlalchemy import create_engine


if __name__ == "__main__":
    
    host='localhost'
    port=3306
    user=sys.argv[1]
    passwd=sys.argv[2]
    db=sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{user}:{passwd}@{host}/{db}', pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).all().orderby(State.id)

    for row in result:
        print("{}: {}".format(row.id, row.name))