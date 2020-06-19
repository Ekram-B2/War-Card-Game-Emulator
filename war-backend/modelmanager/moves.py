
class Moves(db.model):
    __tablename__ = "moves"
    sess_id = db.Column(db.String(200), primary_key=True, default="0")
    user = db.Column(db.String(200))
    move = db.Column(db.Integer())
    time_created = db.Column(
        db.DateTime(), default=datetime.datetime.utcnow)


def create_move(data):
    move = data["move"]
    sess = data["session"]
    user = data["user"]
    new_move = Moves(sess_id=sess, user=user,move=move)
    db.session.add(new_move)
    db.session.commit()
    return new_move

def get_moves(sess_id, user):
    moves = Moves.query.filter_by(sess_id=sess_id, user=user).all()
    return moves

