def run(app):

    # customer
    PREFIX_CUSTOMER = "customer"
    @app.route("/{PREFIX_CUSTOMER}/show", methods=["GET"])
    def show():
        customerController = controllers.CustomerController()
        customerController.show_customer
