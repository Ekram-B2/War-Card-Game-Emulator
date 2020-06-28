from flask import request, jsonify
from flask_restplus import abort, Resource
from api import rest_api
from models.sessionmanager import session_manager
from models.transactionmanager import TransactionManager
from models.restclient import PlayerMovesClient

ns = rest_api.namespace("moves", description="endpoints for managing player moves")

@ns.route("/")
class Moves(Resource):
    def get(self):
        # 1. Apply a query to get all the moves associated to that user
        args = request.args
        transactionManager = TransactionManager()
        client = PlayerMovesClient()
        moves = session_manager.execute_tranaction(transactionManager, client, "get", None)
        # Tranform output to wellformed result
        moves = getWellFormedMoves(moves)
        resp = jsonify({"move": moves})
        resp.status_code = 200
        return resp

    def post(self):
        # 1. Parse and extract object representation of request body
        args = request.form
        # 2. Apply the transaction manager to store into the session data tables
        transactionManager = TransactionManager()
        client = PlayerMovesClient()
        session_manager.execute_tranaction(transactionManager, client, "post", args)
        # # 3. Return the new session id that was stored in the database
        resp = jsonify({"move": args["move"]})
        resp.status_code = 200
        return resp
        
def getWellFormedMoves(moves):
    out_moves = []
    for player_move in moves:
        out_moves.append({"move" : player_move.move})
    return out_moves