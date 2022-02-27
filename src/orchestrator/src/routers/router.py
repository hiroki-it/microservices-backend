# @see https://fastapi.tiangolo.com/tutorial/bigger-applications/#apirouter
# @see https://fastapi.tiangolo.com/tutorial/dependencies/
def create_router():
    from fastapi import APIRouter
    from fastapi.responses import JSONResponse

    router = APIRouter()
    
    @router.get("/checkout/")
    async def checkout():
         return JSONResponse({"Hello" : "World"})

    return router
