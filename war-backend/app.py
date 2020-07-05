from flask import Flask, Blueprint, send_from_directory
from api import rest_api
from models import sessionmanager
from api.session import ns as session_ns
from api.moves import ns as moves_ns
from apidocs.swagger import swagger_blueprint
#from services.socketio import socketio
 
def create_app():
    # 1. Create instance of flask object
    app = Flask(__name__)
        
    # 2.  Create root endpoint to check to see if application is alive
    @app.route("/")
    def serve_root():
        print("received ping for the root directory")
        return "Hello from the hidden world."

    @app.route("/apidocs/<string:path>")
    def serve_api(path):
        return send_from_directory('static', path)

    blueprint = Blueprint('api', __name__, url_prefix='/api')

    # 3. Load APIs onto flask object as blueprints
    rest_api.init_app(blueprint)
    rest_api.add_namespace(session_ns)
    rest_api.add_namespace(moves_ns)

    # 4. Register the populated blueprint with app
    app.register_blueprint(blueprint)

    # 5. Add the OpenAPI blueprint
    app.register_blueprint(swagger_blueprint, url_prefix='/swagger')
    


    return app

if __name__ == "__main__":
    app = create_app()
    if not app:
        print("was not able to create app object - failure in creation sequence")

    print("created app object successfully")
    app.run(host="0.0.0.0",port=8080, debug=False )
