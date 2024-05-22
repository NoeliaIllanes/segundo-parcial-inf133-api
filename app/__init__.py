
from flask import Flask
from app.utils.database import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate = Migrate(app, db)
    jwt = JWTManager(app)

    SWAGGER_URL = '/api/docs'
    API_URL = '/static/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    from app.controllers.user_controller import user_bp
    from app.controllers.task_controller import task_bp

    app.register_blueprint(user_bp, url_prefix='/api')
    app.register_blueprint(task_bp, url_prefix='/api')

    return app
