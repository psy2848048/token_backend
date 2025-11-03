from flask import Flask, make_response, request
from src.token import Token

app = Flask(__name__)


@app.route("/health", methods=["POST", "GET"])
def health():
    return make_response("it's healthy", 200)

# mission 1: implement [get balance]
# - GET /token/{address}
#   - parameter: {address}: address
# - Response
#   - 200
#   - {"balance": <int>}


@app.route("/token/<address>", methods=["GET"])
def get_balance(address):
    token = Token("human fee sting vast car chicken spend distance feature injury toward there")
    value = token.balanceOf(address)
    resp = {
        "balance": value
    }
    return make_response(resp, 200)

# mission 2: implement send
# - POST
# - /token/transfer
# - body: {"to": <address>, "value": <int>}
# - Response
#   - 200
#   - {"tx_hash": <string>}


@app.route("/token/transfer", methods=["POST"])
def transfer():
    # {
    #    "to": <address>,
    #    "value": <int>
    # }
    req_data = request.get_json()
    to = req_data["to"]
    value = req_data["value"]

    token = Token("human fee sting vast car chicken spend distance feature injury toward there")
    tx_hash = token.transfer(to, value)

    resp = {
        "tx_hash": tx_hash
    }

    return make_response(resp, 200)


if __name__ == "__main__":
    app.run("0.0.0.0", 5050)
