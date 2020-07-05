from flask import request, jsonify
from flask_restplus import abort, Resource
from models.models import GameSession
from models.sessionmanager import session_manager
from models.transactionmanager import TransactionManager
from models.restclient import GameSessionClient
from api import rest_api

ns = rest_api.namespace("sessions", description="endpoints for managing sessions")

@ns.route("/")
class Session(Resource):
    def post(self):
        # 1. Parse and extract object representation of request body
        args = request.form
        # 2. Apply the transaction manager to store into the session data tables
        transactionManager = TransactionManager()
        client = GameSessionClient()
        session_manager.execute_tranaction(transactionManager, client, "post", args)
        # Return the new session id that was stored in the database
        resp = jsonify({"session_id": session_id})
        resp.status_code = 200
        return resp

    def get(self):
        # 1. Apply the transaction manager to store into the session data tables
        transactionManager = TransactionManager()
        client = GameSessionClient()
        sessions = session_manager.execute_tranaction(transactionManager, client, "get", None)
        # 2. Convert the sessions to a well formatted form
        sessions = getFormattedSessions(sessions)
        # 3. Return the response
        resp = jsonify({"session": sessions})
        resp.status_code = 200
        return resp

def getFormattedSessions(sessions):
    out_sessions = []
    for session in sessions:
        out_sessions.append({"sess_id": session.sess_id})
    return out_sessions


