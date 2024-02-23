#!/usr/bin/python3
"""Start link class to table in database
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker, scoped_session
import sys
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    found = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            found = True
            break
    if found is False:
        print("Not found")

# if __name__ == "__main__":

#     host = 'localhost'
#     port = 3306
#     user = sys.argv[1]
#     passwd = sys.argv[2]
#     db = sys.argv[3]

#     url = f'mysql+mysqldb://{user}:{passwd}@{host}/{db}'
#     engine = create_engine(url, pool_pre_ping=True)

#     Session = sessionmaker(bind=engine)
#     session = Session()
    # result = session.query(State)
    # a = False
    # for row in result:
    #     if sys.argv[4] == row.name:
    #         print(row.id)
    #         a = True
    #         break
    # if a is False:
    #     print("Not found")
