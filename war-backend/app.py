from flask import Flask, Blueprint
from flask_restplus import Api
#from services.socketio import socketio

def create_app():
    # 1. Create instance of flask object
    app = Flask(__name__)

    # 2. Load APIs onto flask object as blueprints
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api = Api(version='1.0', title='War',
          description='API object for the War Card Game backend APIs')
    api.init_app(app)
    
    # 3. Add name spaces to populate the API object
    ## ... TBD
    ###

    # 4. Register blueprint with app
    app.register_blueprint(blueprint)

    # Create root endpoint for testing purposes
    @app.route("/")
    def serve_root():
        print("Hello World")
        return "Hello world"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="127.0.0.1",port=8080, debug=False )
