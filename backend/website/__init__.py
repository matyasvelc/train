from flask import Flask
from flask_cors import CORS, cross_origin


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SECRET_KEY'] = 'ahoj'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app