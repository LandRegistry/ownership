from ownership import db
from sqlalchemy.dialects.postgresql import UUID

class Owners(db.Model):

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    title_number = db.Column(db.String(10), nullable=False)
    lrid = db.Column(UUID(as_uuid=True), nullable=False)
    owner_index = db.Column(db.Integer(), nullable=False)
