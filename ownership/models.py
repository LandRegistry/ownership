from ownership import db

class Owners(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    title_number = db.Column(db.String())
    lrid = db.Column(db.String())
    owner_index = db.Column(db.Integer())
