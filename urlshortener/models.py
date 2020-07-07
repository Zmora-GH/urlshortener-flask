import datetime
from app import db


class ShortURL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_url = db.Column(db.String(120), index=True, unique=True)
    short_url = db.Column(db.String(120), index=True, unique=True)
    clicks = db.Column(db.Integer, default=0)
    date_added = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f'<URL: id {self.id} url: {self.short_url}>'
