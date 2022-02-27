# @see https://fastapi.tiangolo.com/tutorial/bigger-applications/#apirouter
# @see https://fastapi.tiangolo.com/tutorial/dependencies/
def create_router():
    from fastapi import APIRouter, Depends

    router = APIRouter()

    return router
