from . import db

class Textbook(db.Model):
    __tablename__ = "textbook"

    id = db.Column(db.Integer, primary_key=True)

