from abc import ABC, abstractmethod
from models.models import PlayerMove
from models.models import GameSession

class RestClient(ABC):
    
    @abstractmethod
    def get_from_store(self):
        pass

    @abstractmethod
    def insert_in_store(self, data):
        pass
   
class PlayerMovesClient(RestClient):
    def get_from_store(self, data, session):
        # 1. Get relevant information form the data object
        user_id = data["user_id"]
        # 2. Apply query object to trigger a read to the data store
        moves = session.query(PlayerMove).filter_by(user_id=user_id).all()
        # 3. Return moves
        return moves
    
    def insert_in_store(self, data, session):
        # 1. Get relevant information from the data object
        user_id = data["user_id"]
        move_id = data["move_id"]
        move = data["move"]
        # 2. Create a new grain
        player_move = PlayerMove(move_id=move_id, user_id=user_id, move=move)
        # 3. Add grain to the session registry
        session.add(player_move)
        # 4. Commit transaction
        session.commit()

class GameSessionClient(RestClient):
    def get_from_store(self, data, session):
        # 1. Apply query to trigger read from the data store
        game_sessions = session.query(GameSession).all()
        # 2. Return moves
        return game_sessions
    
    def insert_in_store(self, session_id, session):
        # 1. Create a new grain
        game_session = GameSession(sess_id=session_id)
        # 2. Add grain to the session registry
        session.add(game_session)
        # 4. Commit transaction
        session.commit()
