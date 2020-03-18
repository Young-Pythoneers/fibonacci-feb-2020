from pathlib import Path

from connexion import FlaskApp
from flask import Flask

from fibonacci.models import db
from fibonacci.routes import site


def create_app(config: str) -> Flask:
    """Creates a new FlaskApp instance

    Args:
        config: Config module name. e.g. `config.prod`

    Returns:
        Configured FlaskApp
    """
    api = FlaskApp(__name__, specification_dir=Path() / "swagger")
    api.add_api("swagger.yml")

    # Get `Flask` object
    app = api.app

    app.config.from_object(config)
    app.register_blueprint(site.mod)

    db.init_app(app)

    return app


if __name__ == "__main__":
    flask_app = create_app("config.prod")

    db.create_all(app=flask_app)

    flask_app.run()
