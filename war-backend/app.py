from flask import Flask, Blueprint
from flask_restplus import Api
#from services.socketio import socketio

def create_app():
    # Create instance of flask object
    app = Flask(__name__)
    # Load APIs onto flask object as blueprints
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api = Api(version='1.0', title='War',
          description='API object for the War Card Game backend APIs')
    api.init_app(app)
    # add name spaces to populate the API object
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="127.0.0.1",port=8080, logging=True, debug=False )
