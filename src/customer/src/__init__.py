from fastapi import FastAPI
from dotenv import load_dotenv

def create_app():
    from src.routers.router import set_routes

    load_dotenv()

    app = FastAPI()
    
    router = set_routes()
    
    app.include_router(router)

    return app
