import json

from wiki.app import db


class FRecord(db.Model):
    __tablename__ = 'frecord'

    id = db.Column(db.Integer, primary_key=True)
    parent_dir = db.Column(db.String(512))
    fname = db.Column(db.String(256))

    def __repr__(self):
        return json.dumps({
            'id': self.id,
            'parent_dir': self.parent_dir,
            'fname': self.fname
        })