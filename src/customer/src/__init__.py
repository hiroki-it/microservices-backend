from dotenv import load_dotenv
from flask import Flask
from src.infrastructure.routers.router import test

def create_app():
    app = Flask(__name__)
    test()
    return app
