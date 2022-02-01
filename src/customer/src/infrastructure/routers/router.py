from src.interface.controllers.customer_controller import CustomerController

def set_routes(app):

    # customer
    PREFIX_CUSTOMER = "customers"
    @app.route("/{PREFIX_CUSTOMER}/show", methods=["GET"])
    customerController = CustomerController()
    customerController.show_customer()
