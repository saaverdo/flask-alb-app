import os
from flask import render_template, request, session, redirect, url_for, current_app
from datetime import datetime
from .. import db
from ..models import Record
from . import main

HOSTNAME = os.uname()[1]

@main.route('/')
@main.route('/index')
def index():
    remote_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    hostname=HOSTNAME
    record = Record(hostname=hostname,
                    remote_ip=remote_ip,
                    date=datetime.utcnow()
    )
    db.session.add(record)
    db.session.commit()
    return render_template('index.html', hostname=hostname, remote_ip=remote_ip, current_time=datetime.utcnow())

@main.route("/display")
def display():
    records = [record.to_dict() for record in Record.query.all()]
    print(records)
    # t_data = cursor.fetchall()	
    # return render_template("display.html", t_data = t_data)
    return redirect(url_for('.index'))

@main.route("/healthcheck")
def healthcheck():
    return "ok", 200