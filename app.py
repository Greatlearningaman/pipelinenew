from flask import Flask, request
from flask_restx import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

# * Calculator API
api = Api(
    app,
    version="1.1",
    title="Calculator API",
    description="A simple calculator API that performs basic mathematical operations",
)

ns = api.namespace("arithops", description="Arithmetic operations")

arith_op = api.model(
    "ArithOp",
    {
        "id": fields.Integer(
            readonly=True, description="Unique identifier of operations history"
        ),
        "a": fields.Integer(required=True, description="First arithmetic operand"),
        "b": fields.Integer(required=True, description="Second arithmetic operand"),
        "result": fields.Integer(
            readonly=True, description="Result of arithmetic operation"
        ),
        "op": fields.String(readonly=True, description="Arithmetic operation symbol"),
    },
)


class ArithOpsHistory(object):
    def __init__(self):
        self.counter = 0
        self.arithops = []

    def get(self, id):
        for arithop in self.arithops:
            if arithop["id"] == id:
                return arithop
        api.abort(404, "Arithop {} doesn't exist".format(id))

    def create(self, data):
        arithop = data
        arithop["id"] = self.counter = self.counter + 1
        self.arithops.append(arithop)
        return arithop


history = ArithOpsHistory()


@ns.route("/")
class TodoList(Resource):
    """Shows a list of all arithmetic operations possible"""

    @ns.doc("list_arithops")
    @ns.marshal_list_with(arith_op)
    def get(self):
        """List all arithmetic operations performed so far"""
        return history.arithops


@ns.route("/<int:id>")
@ns.response(404, "Arthimetic Operational History not found")
@ns.param("id", "The arithop identifier")
class Todo(Resource):
    """Show a single arithop item"""

    @ns.doc("get_arithop")
    @ns.marshal_with(arith_op)
    def get(self, id):
        """Fetch a given arithop"""
        return history.get(id)


@ns.route("/add")
class Add(Resource):
    """Add two numbers"""

    @ns.doc("add")
    @ns.expect(arith_op)
    def post(self):
        payload = request.get_json()
        payload["op"] = "add"
        payload["result"] = payload["a"] + payload["b"]
        return history.create(payload)


@ns.route("/subtract")
class Subtract(Resource):
    """Subtract two numbers"""

    @ns.doc("subtract")
    @ns.expect(arith_op)
    def post(self):
        payload = request.get_json()
        payload["op"] = "subtract"
        payload["result"] = payload["a"] - payload["b"]
        return history.create(payload)


@ns.route("/multiply")
class Multiply(Resource):
    """Multiply two numbers"""

    @ns.doc("multiply")
    @ns.expect(arith_op)
    def post(self):
        payload = request.get_json()
        payload["op"] = "multiply"
        payload["result"] = payload["a"] * payload["b"]
        return history.create(payload)


@ns.route("/divide")
class Divide(Resource):
    """Divide two numbers"""

    @ns.doc("divide")
    @ns.expect(arith_op)
    def post(self):
        payload = request.get_json()
        payload["op"] = "divide"
        if payload["b"] != 0:
            payload["result"] = payload["a"] / payload["b"]
        else:
            payload["result"] = ""
        return history.create(payload)


if __name__ == "__main__":
    app.run()
