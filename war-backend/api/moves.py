from flask import request
from flask_restplus import abort, Resource
from modelmanager.business import create_move, get_moves
from sessions import ns

@ns.route("/<int:sess_id>/moves")
class Moves(Resource):
    def get(self, sess_id):
        # 1. Get userId as a query parameter
        
        # 2. Apply a query to get all the moves associated to that user
        return get_moves(id, "1")

@ns.route("/<int:sess_id/moves/move<int:move_num>")
class Move(Resource):
    def post(self, sess_id, move_num):
        # 1. Parse arguments
        args = parse(request)
        # 2. Extract required data
        move = args["move"]
        user = args["user"]
        # 3. Create a model of the data
        data = {
            "move": move,
            "session": sess,
            "user": user
        }
        isCreated = create_move(data)
        # 4. Use the nility of the return to determine whether the status was created successfully or not
        if not isCreated:
            abort(httpInternalServerError, 'Cannot create new status')
            return
        # 5. Return a result back to client
        return {"move_added": move}




