

class Session(db.Model):
    __tablename__ = 'sessions'
    sess_id = db.Column(db.String(200), primary_key=True, default="0")
    time_created = db.Column(
        db.DateTime(), default=datetime.datetime.utcnow)
       
    def __repr__(self):
        return '<Session %r>' % self.sess_id

"""
Create a new session
"""
def create_session(data):
    session_id = data.get('sess_id')
    session = Session(sess_id=session_id)
    db.session.add(session)
    db.session.commit()
    return session
 
