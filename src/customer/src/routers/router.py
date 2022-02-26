# @see https://fastapi.tiangolo.com/tutorial/bigger-applications/#apirouter
# @see https://fastapi.tiangolo.com/tutorial/dependencies/
def set_routes():
    from fastapi import APIRouter, Depends
    from sqlalchemy.orm import Session
    from src.database.db import get_db
    from src.controllers.customer_controller import CustomerController

    router = APIRouter()

    # customer
    PREFIX_CUSTOMER = "customers"

    @router.get("/{PREFIX_CUSTOMER}/")
    async def route_index_customer(db: Session = Depends(get_db)):
        customerController = CustomerController(db)
        return customerController.index_customer()

    @router.post("/{PREFIX_CUSTOMER}/")
    async def route_create_customer(db: Session = Depends(get_db)):
        customerController = CustomerController(db)
        return customerController.create_customer()

    return router
