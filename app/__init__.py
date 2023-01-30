from flask import Flask
import os

def _initialize_blueprints(app):
    from app.routes.employee import employees
    app.register_blueprint(employees)

def create_app() -> Flask:
    app = Flask(__name__)
    _initialize_blueprints(app)
    return app


