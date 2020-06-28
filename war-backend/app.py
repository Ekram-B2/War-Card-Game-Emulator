from flask import Flask, Blueprint
from api import rest_api
from models import sessionmanager
from api.session import ns as session_ns
from api.moves import ns as moves_ns
#from services.socketio import socketio

def create_app():
    # 1. Create instance of flask object
    app = Flask(__name__)
        
    # 2.  Create root endpoint to check to see if application is alive
    @app.route("/")
    def serve_root():
        print("received ping for the root directory")
        return "Hello from the hidden world."

    blueprint = Blueprint('api', __name__, url_prefix='/api')

    # 3. Load APIs onto flask object as blueprints
    rest_api.init_app(blueprint)
    rest_api.add_namespace(session_ns)
    rest_api.add_namespace(moves_ns)
    # 4. Add name spaces to populate the API object

    # 5. Register blueprint with app
    app.register_blueprint(blueprint)


    return app

if __name__ == "__main__":
    app = create_app()
    if not app:
        print("was not able to create app object - failure in creation sequence")

    print("created app object successfully")
    app.run(host="0.0.0.0",port=8080, debug=False )
