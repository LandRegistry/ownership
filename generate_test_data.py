from ownership.models import Owners
from ownership import db, app
from flask.ext.sqlalchemy import SQLAlchemy
import os

os.environ['DATABASE_URL']='postgresql://localhost/ownership'

app.config.from_object('config.DevelopmentConfig')

def create_user(id, title_number, lrid, owner_index):
    owner = Owners()
    owner.id = id
    owner.title_number = title_number
    owner.lrid = lrid
    owner.owner_index = owner_index
    return owner

#Delete data first
Owners.query.delete()

#Now insert some data
db.session.add(create_user(1, 'DN100', '1234', 1))
db.session.add(create_user(2, 'DN100', '1235', 2))
db.session.add(create_user(3, 'DN101', '1236', 1))
db.session.add(create_user(4, 'DN102', '1237', 1))
db.session.add(create_user(5, 'DN102', '1238', 2))
db.session.add(create_user(6, 'DN102', '1239', 3))

db.session.commit()
