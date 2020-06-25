import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class PlayerMove(base):
    __tablename__ = "player_moves"
    move_id = Column(String(200), primary_key=True, default="0")
    user_id = Column(String(200))
    move = Column(Integer())
    time_created_at = Column(
        DateTime(), default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<player_move {}>'.format(self.move_id)

class GameSession(base):
    __tablename__ = 'game_sessions'
    sess_id = Column(String(200), primary_key=True, default="0")
    time_created_at = Column(
        DateTime(), default=datetime.datetime.utcnow)
       
    def __repr__(self):
        return '<game_session {}>'.format(self.sess_id)