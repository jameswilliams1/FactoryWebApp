from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    from project.api.views import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/products')
    app.app_context().push()
    return app
