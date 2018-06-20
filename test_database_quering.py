import cherrypy, os
import sqlite3
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker

from test_database_webinterface import Base, Person

engine = create_engine('sqlite:///C:\\Users\\cphnano\\paul lebaigue\\first database\\person.db')

class delete_database:


    # ---------------index
    @cherrypy.expose
    def index(self, button=None, ID_="", **params):

        if button:
            # enable the access for DBSession
            Base.metadata.bind = engine

            # Create a conversation with the database
            DBSession = sessionmaker(bind=engine)
            session = DBSession()

            # Delete in the database
            p2kill=session.query(Person).filter(Person.id == ID_).one()
            session.delete(p2kill)

            session.commit()
            session.close()

        mypage = str(open('mypage.html').read())
        output = mypage % ID_
        return output


if __name__ == '__main__':
    cherrypy.quickstart(delete_database())
