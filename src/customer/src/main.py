from dotenv import load_dotenv
from flask import Flask
from infrastructure.routers.router import run

load_dotenv(override=True)

app = Flask(__name__)

if __name__ == '__main__':
    run(app)
