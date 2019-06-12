from app import db


class Contacts(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(20))
    tel = db.Column(db.String(12))
