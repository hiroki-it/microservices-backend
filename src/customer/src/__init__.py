from fastapi import FastAPI

def create_app():
    from src.infrastructure.routers.router import set_routes

    app = FastAPI()
    set_routes(app)
    return app
