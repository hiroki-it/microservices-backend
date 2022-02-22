from fastapi import jsonify

class CustomerController:

    def index_customer(self):
        return jsonify({ "name" : "foo" })
