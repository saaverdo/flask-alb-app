from flask import render_template, session, redirect, url_for, current_app
from datetime import datetime
from .. import db
from ..models import Record
from . import main

@main.route('/')
@main.route('/index')
def index():
    remote_ip = request.remote_addr if request.headers.get('X-Forwarded-For') == 'None' else request.headers.get('X-Forwarded-For')
    record = Record(hostname=
                    remote_ip=
                    date=datetime.utcnow()
            db.session.add(user)
            db.session.commit()
    cursor.execute('INSERT INTO requests VALUES (NULL, % s, % s, %s)', (Config.HOSTNAME, request.remote_addr, str(datetime.today())))
    mysql.connection.commit()
    return render_template('index.html', hostname=Config.HOSTNAME, remote_ip=remote_ip, current_time=datetime.utcnow())

@main.route("/display")
def display():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM requests',)
    t_data = cursor.fetchall()	
    return render_template("display.html", t_data = t_data)


@main.route("/healthcheck")
def healthcheck():
    return "ok", 200