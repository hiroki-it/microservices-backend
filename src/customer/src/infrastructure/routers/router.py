from src.interface.controllers.customer_controller import CustomerController

def set_routes(app):

    # customer
    PREFIX_CUSTOMER = "customers"
    customerController = CustomerController()
    @app.route("/{PREFIX_CUSTOMER}/", methods=["GET"])
    def index_customer():
        return customerController.index_customer()
