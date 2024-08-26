from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
# other imports here
# import prometheus_client
# from flask_prometheus_metrics import register_metrics
from prometheus_flask_exporter import PrometheusMetrics
# pre-init modules
bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()
metrics = PrometheusMetrics.for_app_factory()
import structlog
import logging 

log = structlog.get_logger()
# logger = logging.getLogger()

# # logging.getLogger("netmiko").setLevel(logging.WARNING)
# logging.basicConfig(
#     format="%(threadName)s %(levelname)s: %(message)s",
#     level=logging.INFO,
# )
#             log.error('zipkin_error',
#                       service='post',
#                       traceback=tb)
# logging.info(f'Connecting to {ip}')

def create_app(config_name):
    app = Flask(__name__)
    # app.logger.info(f'Service appka started with config: {config_name}')
    # print(f'creating app with config = {config_name}')
    # config_name = 'default'
    config[config_name].CONFIG_NAME = config_name
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    metrics.init_app(app)
    
    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    # if config_name in ['default', 'mysql']:
    log.info(app.config['APP_NAME'], message=f'"App started with config: {config_name}"')
    # app.logger.info(f'Service appka started with config: {config_name}')
    #     logging.info(f'Service appka started with config={config_name}')
    

    app_context = app.app_context()
    app_context.push()
    db.create_all()

    metrics.info('app_info', 'Application info', version='0.0.3-metrics')
    metrics.info('app_config', 'Application config', config=f'{config_name}')
    # prometheus metrics
    # app.post_read_db_seconds = prometheus_client.Histogram(
    #     'post_read_db_seconds',
    #     'Request DB time'
    # )
    # app.views_count = prometheus_client.Counter(
    #     'views_count',
    #     'A counter of page views'
    # )
    # if config_name == 'mysql':
    #     app_context = app.app_context()
    #     app_context.push()
    #     db.create_all()

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app
