from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman

from service.routes import accounts_blueprint


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.update(
        TESTING=False,
        TALISMAN_FORCE_HTTPS=False,
    )
    if test_config:
        app.config.update(test_config)

    # CORS is enabled for the API. Restrict origins to your frontend in production.
    CORS(app, resources={r"/accounts*": {"origins": "*"}})

    # Security headers are set by Talisman. HTTPS enforcement stays off for local labs.
    Talisman(
        app,
        force_https=app.config.get("TALISMAN_FORCE_HTTPS", False),
        content_security_policy={
            "default-src": ["'self'"],
            "object-src": ["'none'"],
            "frame-ancestors": ["'none'"],
        },
    )

    app.register_blueprint(accounts_blueprint)
    return app
