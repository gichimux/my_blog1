from flask import Flask
from flask_babel import Babel
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager
from flask_pagedown import PageDown
from flask_moment import Moment
from flask_whooshee import Whooshee
from config import config_options
from flask_bootstrap import Bootstrap

babel = Babel()
db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

pagedown = PageDown()
moment = Moment()
mail = Mail()
whooshee = Whooshee()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    # config[config_name].init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    pagedown.init_app(app)
    whooshee.init_app(app)
    bootstrap.init_app(app)

    if not app.debug and not app.testing and not app.config['SSL_DISABLE']:
        from flask_sslify import SSLify
        sslify = SSLify(app)

    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    from .admin import admin as admin_blueprint
    from .message import message as message_blueprint
    from .api import api as api_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    app.register_blueprint(message_blueprint, url_prefix='/message')
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app