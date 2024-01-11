import os
from datetime import datetime
from config import Config
from flask import Flask, render_template, json, request, redirect, url_for, session
from flask_bootstrap import Bootstrap
from flask_moment import Moment



app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
@app.route('/index')
def index():
    remote_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    return render_template('index.html', hostname=Config.HOSTNAME, remote_ip=remote_ip, current_time=datetime.utcnow())


@app.route("/healthcheck")
def healthcheck():
    return "ok", 200

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('404.html'), 500

if __name__ == "__main__":
    app.run()
