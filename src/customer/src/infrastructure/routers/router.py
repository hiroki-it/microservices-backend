from src.interface.controllers.customer_controller import CustomerController

def set_routes(app):

    # customer
    PREFIX_CUSTOMER = "customers"
    customerController = CustomerController()
    @app.route("/{PREFIX_CUSTOMER}/show", methods=["GET"])
    def show():
        customerController.index_customer()
