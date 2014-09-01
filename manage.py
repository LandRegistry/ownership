import os

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from ownership.models import *
from ownership import app
from ownership import db

app.config.from_object(os.environ['SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.option('--lrid', dest='lrid')
@manager.option('--owner_index', dest='owner_index')
@manager.option('--title_number', dest='title_number')
def create_owner(lrid, owner_index, title_number):
    owner = Owners()
    owner.lrid = lrid
    owner.owner_index = owner_index
    owner.title_number = title_number

    db.session.add(owner)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
