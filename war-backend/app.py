from flask import Flask, Blueprint
#from flask_restplus import Api
from databaseclient import client
#from services.socketio import socketio

def create_app():
    # 1. Create instance of flask object
    app = Flask(__name__)

    # 2. Test connection with SqlLite instance
    db_client = client.get_database_client("sqlite", "/root/sqlite.db")
    db_client.test_connection()
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
    app.run(host="0.0.0.0",port=8080, debug=False )
