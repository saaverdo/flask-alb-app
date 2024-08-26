import os
from app import create_app, db
from app.models import Record
import logging

config_name = os.environ.get('FLASK_CONFIG', 'default')
# print(f'config = {config_name}')
app = create_app(config_name)


if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.info')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Record=Record)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8000)
