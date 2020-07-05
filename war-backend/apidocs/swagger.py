from flask_swagger_ui import get_swaggerui_blueprint

API_URL = '/static/swagger.json'

swagger_blueprint = get_swaggerui_blueprint('/swagger', API_URL, config = {
    'app_name': "War Backend Interface"
})
