#!/usr/bin/python3
'''state script'''

from model_state import Base, State
from sqlalchemy.orm import sessionmaker, scoped_session
import sys
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    state_to_update = session.query(State).filter_by(id=2).first()
    # Update the name attribute
    state_to_update.name = 'New Mexico'
    session.commit()
