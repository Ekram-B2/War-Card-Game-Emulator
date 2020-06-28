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
    def get_from_store(self, session): 
        # 1. Apply query object to trigger a read to the data store
        moves = session.query(PlayerMove).all()
        # 2. Return moves
        return moves
    
    def insert_in_store(self, data, session):
        # 1. Get relevant information from the data object
        move = data["move"]
        # 2. Create a new grain
        largestId = session.query(PlayerMove).order_by(PlayerMove.move_id).limit(1)
        player_move = PlayerMove(move=move)
        # 3. Add grain to the session registry
        session.add(player_move)
        # 4. Commit transaction
        session.commit()

class GameSessionClient(RestClient):
    def get_from_store(self, session):
        # 1. Apply query to trigger read from the data store
        game_sessions = session.query(GameSession).all()
        # 2. Return moves
        return game_sessions
    
    def insert_in_store(self, data, session):
        # 1. Create a new grain
        session_id = data["sess_id"]
        game_session = GameSession(sess_id=session_id)
        # 2. Add grain to the session registry
        session.add(game_session)
        # 4. Commit transaction
        session.commit()
