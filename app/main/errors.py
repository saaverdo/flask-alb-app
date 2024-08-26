from flask import render_template, current_app
from . import main
import structlog

log = structlog.get_logger()

@main.app_errorhandler(404)
def page_not_found(e):
    log.error(current_app.config['APP_NAME'], error=e)
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    log.error(current_app.config['APP_NAME'], error=e)
    return render_template('500.html'), 500