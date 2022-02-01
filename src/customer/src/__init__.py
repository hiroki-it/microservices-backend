from dotenv import load_dotenv
from flask import Flask
from src.infrastructure.routers.router import set_routes

def create_app():
    app = Flask(__name__)
    set_routes(app)
    return app
