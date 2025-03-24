from flask import Flask
from src.routes.main_bp import main_bp
from src.utils.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(main_bp, url_prefix='/api')
    return app