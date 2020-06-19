from flask import request
from flask_restplus import abort, Resource
from modelmanager.business import create_session


ns = api.namespace("sessions", description="endpoints for managing content within sessions)

@ns.route("/session/<int:sess_id>")
class Session(Resource):
    def post(self, id):
        # 1. Parse and extract object representation of request body
        args = parse(request)
        session_id = args["sess_id"]
        # 2. Create a new model instance of the session
        isCreated = create_session({
            "name": id 
        })
        # 3. Use nility of the return to detemine whether one was created or not
        if not isCreated:
            abort(httpInternalServerError, 'Cannot create new status')
            return
        # Return a session
        return {"session_id": args["session_id"]}


