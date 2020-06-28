from flask_restplus import Api

# Main API manager object 
rest_api = Api(version='1.0', title='War Card Game',
          description='API object for the War Card Game server side')