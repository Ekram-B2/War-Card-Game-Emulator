import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class ModelManager:
    def __init__(self, connection_string=""):
        self.connection_string = connection_string
        self.engine = create_engine(self.connection_string)

    def create_tables(self):
        base.metadata.create_all(self.engine)

    def get_sessions(self):
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        return session.query(Moves).all()


class Moves(base):
    __tablename__ = "moves"
    move_id = Column(String(200), primary_key=True, default="0")
    user = Column(String(200))
    move = Column(Integer())
    time_created_at = Column(
        DateTime(), default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<session {}>'.format(self.move_id)

class Session(base):
    __tablename__ = 'sessions'
    sess_id = Column(String(200), primary_key=True, default="0")
    time_created_at = Column(
        DateTime(), default=datetime.datetime.utcnow)
       
    def __repr__(self):
        return '<session {}>'.format(self.sess_id)