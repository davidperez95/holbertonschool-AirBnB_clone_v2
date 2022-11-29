#!/usr/bin/pythin3
""""""
import os
from sqlalchemy import create_engine


os.environ["HBNB_MYSQL_USER"] = "hbnb_dev"
os.environ["HBNB_MYSQL_PWD"] = "hbnb_dev_pwd"
os.environ["HBNB_MYSQL_HOST"] = "localhost"
os.environ["HBNB_MYSQL_DB"] = "hbnb_dev_db"

class DBStorage:
    __engine = None
    __session = None
    

    def __init__(self):
        self.__engine = "mysql+mysqldb://{}:{}@{}/{}"\
            .format(os.getenv("HBNB_MYSQL_USER"),\
                    os.getenv("HBNB_MYSQL_PWD"),\
                    os.getenv("HBNB_MYSQL_HOST"),\
                    os.getenv("HBNB_MYSQL_DB")
                    )

        engine = create_engine(self.__engine)