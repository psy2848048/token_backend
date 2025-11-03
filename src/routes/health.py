from flask import Blueprint, make_response
from src.services.health import health as health_service

health_bp = Blueprint("health", __name__, url_prefix="/health")


@health_bp.route("/", methods=["GET"])
def health():
    message = health_service()
    return make_response(message, 200)


@health_bp.route("/<name>", methods=["GET"])
def print_my_name(name):
    return make_response(name, 200)
