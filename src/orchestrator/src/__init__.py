def create_app():
    from fastapi import FastAPI
    from src.routers.router import create_router

    app = FastAPI()
    
    router = create_router()
    
    app.include_router(router)

    return app
