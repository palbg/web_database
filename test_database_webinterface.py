import cherrypy, os
import sqlite3
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker

# creation of the database
Base = declarative_base()


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    firstname = Column(String(255), nullable=False)
    lastname = Column(String(255), nullable=False)
    position = Column(String(255), nullable=False)

    def __init__(self, id=None, firstname=None, lastname=None, position=None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.position = position


engine = create_engine('sqlite:///C:\\Users\\cphnano\\paul lebaigue\\first database\\person.db')
Base.metadata.create_all(engine)

# _______________________________________________________________

# the front page of the website
mypage = """
<h1>Register a new member of cphnano</h1>

<form action="index" method="GET">
<p>ID</p>
<input type=integer name="ID_" value= %s>

<p>Firstname</p>
<input type=string name="firstname_" value= %s>

<p>Lastname</p>
<input type=string name="lastname_" value= %s>

<p>Position</p>
<input type=string name="position_" value= %s>

<input type=submit name=button value="insert in database">

</form>

<br>
<hr>
"""


class web_database:

    # ---------------index
    @cherrypy.expose
    def index(self, button=None, ID_="", firstname_="", lastname_="", position_="" ,**params):

        if button:
            # enable the access for DBSession
            Base.metadata.bind = engine

            # Create a conversation with the database
            DBSession = sessionmaker(bind=engine)
            session=DBSession()

            # Insert a Person in the person table
            new_person = Person(id=ID_,
                                firstname=firstname_,
                                lastname=lastname_,
                                position=position_)

            # Add in the database
            session.add(new_person)
            session.commit()
            session.close()

        output = mypage % (ID_, firstname_, lastname_, position_)
        return output


if __name__ == '__main__':
    cherrypy.quickstart(web_database())
