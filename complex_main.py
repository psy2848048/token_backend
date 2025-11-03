from flask import Flask
from src.routes.health import health_bp
from src.routes.token import token_bp


app = Flask(__name__)


def create_app():
    app.register_blueprint(health_bp)
    app.register_blueprint(token_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5050)
