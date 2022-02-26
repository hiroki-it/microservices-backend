from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

def set_routes():
    from src.database.db import get_db
    from src.controllers.customer_controller import CustomerController

    router = APIRouter()

    # customer
    PREFIX_CUSTOMER = "customers"
    customerController = CustomerController()

    @router.get("/{PREFIX_CUSTOMER}/")
    def route_index_customer():
        return customerController.index_customer()

    @router.post("/{PREFIX_CUSTOMER}/")
    def route_create_customer():
        return customerController.create_customer()
