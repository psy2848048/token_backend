from flask import Flask, make_response

app = Flask(__name__)

@app.route("/health")
def health():
    return make_response("it's healthy", 200)

# mission 1: implement [get balance]
# - GET /token/{address}
#   - parameter: {address}: address
# - Response
#   - 200
#   - {"balance": <int>}

# mission 2: implement send
# - POST
# - /token/transfer
# - body: {"to": <address>, "value": <int>}
# - Response
#   - 200
#   - {"tx_hash": <string>}


if __name__ == "__main__":
    app.run("0.0.0.0", 5050)
