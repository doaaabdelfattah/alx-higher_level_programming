#!/usr/bin/python3
"""Start link class to table in database 
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker, scoped_session
import sys
from sqlalchemy import create_engine

host='localhost'
port=3306
user=sys.argv[1]
passwd=sys.argv[2]
db=sys.argv[3]
if __name__ == "__main__":
#  # The string form of the URL is dialect[+driver]://user:password@host/dbname[?key=value..],
    engine = create_engine(f'mysql+mysqldb://{user}:{passwd}@{host}/{db}', pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).all().orderby(State.id)

    for row in result:
        print(f'{row.id}: {row.name}')