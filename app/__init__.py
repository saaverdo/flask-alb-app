from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
# other imports here

# pre-init modules
bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    print(f'config = {config_name}')
    config_name = 'default'
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    
    if config_name == 'default':
        app_context = app.app_context()
        app_context.push()
        db.create_all()

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app
