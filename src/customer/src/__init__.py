def create_app():
    from fastapi import FastAPI
    from dotenv import load_dotenv
    from src.routers.router import create_router

    load_dotenv()

    app = FastAPI()
    
    router = create_router()
    
    app.include_router(router)

    return app
