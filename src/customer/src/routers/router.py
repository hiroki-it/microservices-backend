from fastapi import Depends
from sqlalchemy.orm import Session
from src.database.db import get_db

def set_routes(app):
    from src.controllers.customer_controller import CustomerController

    # customer
    PREFIX_CUSTOMER = "customers"
    customerController = CustomerController()

    @router.get("/{PREFIX_CUSTOMER}/")
    def route_index_customer():
        return customerController.index_customer()

    @router.post("/{PREFIX_CUSTOMER}/")
    def route_create_customer():
        return customerController.create_customer()
