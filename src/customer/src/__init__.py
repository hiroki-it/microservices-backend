from flask import Flask

def create_app():
    from src.infrastructure.routers.router import set_routes

    app = Flask(__name__)
    set_routes(app)
    return app
