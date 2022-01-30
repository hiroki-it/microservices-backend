from flask import Flask

PREFIX_CUSTOMER = "customer"

def run():
    app = Flask(__name__)
    
    # customer
    @app.route("/{PREFIX_CUSTOMER}/show", methods=["GET"])
    def show():
        customerController = controllers.CustomerController()
        customerController.show_customer
