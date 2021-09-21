from flask import Flask

from .vaccination_view import bp as bp_vaccine


def init_app(app: Flask):
    app.register_blueprint(bp_vaccine)
