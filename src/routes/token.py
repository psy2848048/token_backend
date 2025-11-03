from flask import Blueprint, make_response, request
from src.services.token import get_balance as get_balance_service, transfer as transfer_service

token_bp = Blueprint("token", __name__, url_prefix="/token")


@token_bp.route("/<address>", methods=["GET"])
def get_balance(address):
    value = get_balance_service(address)
    resp = {
        "value": value
    }
    return make_response(resp, 200)


@token_bp.route("/transfer", methods=["POST"])
def trasnfer():
    req_data = request.get_json()
    to = req_data["to"]
    value = req_data["value"]

    tx_hash = transfer_service(to, value)
    resp = {
        "tx_hash": tx_hash
    }
    return make_response(resp, 200)
