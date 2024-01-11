from . import db

class Record(db.Model):
    __tablename__ = 'requests'
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(64))
    remote_ip = db.Column(db.String(20))
    date = db.Column(db.String(100))

    def __repr__(self):
        return '<requests %r>' % self.name
    