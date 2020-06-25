from flask import Flask, Blueprint
#from flask_restplus import Api
from models import modelmanager
#from services.socketio import socketio

def create_app():
    # 1. Create instance of flask object
    app = Flask(__name__)
    
    # 2. Create ORM interface to data
    session_manager = modelmanager.SessionManager("sqlite:////root/sqlite.db")
    session_manager.create_tables()
    # 3. Load APIs onto flask object as blueprints
    # blueprint = Blueprint('api', __name__, url_prefix='/api')
    # api = Api(version='1.0', title='War',
    #       description='API object for the War Card Game backend APIs')
    # api.init_app(app)

    # # 4. Add name spaces to populate the API object
    # ## ... TBD
    # ###

    # # 4. Register blueprint with app
    # app.register_blueprint(blueprint)

    # Create root endpoint for testing purposes
    @app.route("/")
    def serve_root():
        print("received ping for the root directory")
        return "hello from the hidden world"

    return app

if __name__ == "__main__":
    app = create_app()
    if not app:
        print("was not able to create app object - failure in creation sequence")
    
    print("created app object successfully")
    app.run(host="0.0.0.0",port=8080, debug=False )
