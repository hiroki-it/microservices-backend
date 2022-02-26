def set_routes(app):
    from src.controllers.customer_controller import CustomerController

    # customer
    PREFIX_CUSTOMER = "customers"
    customerController = CustomerController()

    @app.route("/{PREFIX_CUSTOMER}/", methods=["GET"])
    def route_index_customer(self):
        return customerController.index_customer()

    @app.route("/{PREFIX_CUSTOMER}/", methods=["POST"])
    def route_create_customer(self):
        return customerController.create_customer()
