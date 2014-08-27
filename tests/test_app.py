from ownership import server, db
from ownership.models import Owners
from flask import request
import unittest
import json
import mock


class OwnershipTestCase(unittest.TestCase):

    def create_user(self, id, title_number, lrid, owner_index):
        owner = Owners()
        owner.id = id
        owner.title_number = title_number
        owner.lrid = lrid
        owner.owner_index = owner_index
        return owner

    def setUp(self):
        db.create_all()
        server.app.config['TESTING'] = True
        self.app = server.app.test_client()
        db.session.add(self.create_user(1, 'DN100', '1234', 1))
        db.session.add(self.create_user(2, 'DN100', '1235', 2))
        db.session.add(self.create_user(3, 'DN101', '1236', 1))
        db.session.add(self.create_user(4, 'DN102', '1237', 1))
        db.session.add(self.create_user(5, 'DN102', '1238', 2))
        db.session.add(self.create_user(6, 'DN102', '1239', 3))
        db.session.commit()

    def test_server(self):
        response = self.app.get('/')
        assert response.status == '200 OK'

    def test_get_owners(self):
        data = json.dumps({"title_number":"DN100"})
        response = self.app.post('/owners', data=data, content_type='application/json')
        assert response.data == '{"owners": [{"index": 1, "lrid": "1234"}, {"index": 2, "lrid": "1235"}]}'
        assert response.status == '200 OK'

    def test_no_owner_found(self):
        data = json.dumps({"title_number":"DN200"})
        response = self.app.post('/owners', data=data, content_type='application/json')
        assert response.data == '{"owners": []}'
        assert response.status == '200 OK'

    def test_bad_request(self):
        data = json.dumps({"title_incorrect_spelling":"DN100"})
        response = self.app.post('/owners', data=data, content_type='application/json')
        assert response.data == 'title_number field not found'
        assert response.status == '400 BAD REQUEST'

    def test_incorrect_content_type(self):
        data = json.dumps({"title_number":"DN100"})
        response = self.app.post('/owners', data=data)
        assert response.status == '415 UNSUPPORTED MEDIA TYPE'

    def test_for_invalid_json(self):
        response = self.app.post('/owners', data='{"title_number":DN', content_type='application/json')
        assert response.status == '400 BAD REQUEST'

    def tearDown(self):
        Owners.query.delete()
        db.session.commit()
