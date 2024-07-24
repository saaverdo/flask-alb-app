import os
from flask import render_template, request, session, redirect, url_for, current_app, Response
from datetime import datetime
from .. import db
from ..models import Record
from . import main
import prometheus_client


# VIEWS_COUNT = prometheus_client.Counter('views_count', 'A counter of page views')


@main.route('/')
@main.route('/index')
def index():
    remote_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    hostname = current_app.config['HOSTNAME']
    record = Record(hostname=hostname,
                    remote_ip=remote_ip,
                    date=datetime.utcnow()
    )
    
    db.session.add(record)
    db.session.commit()
    config_name = current_app.config['CONFIG_NAME']
    # VIEWS_COUNT.inc()
    # current_app.view_count.inc()
    return render_template('index.html', hostname=hostname, remote_ip=remote_ip, current_time=datetime.utcnow(), stage=config_name)

@main.route("/display")
def display():
    records = [record.to_dict() for record in Record.query.all()]
    return render_template("display.html", t_data = records)

@main.route("/healthcheck")
def healthcheck():
    return "ok", 200

# Prometheus endpoint
# @main.route('/metrics')
# def metrics():
#     return Response(prometheus_client.generate_latest(),
#                     mimetype=current_app.config['CONTENT_TYPE_LATEST'])