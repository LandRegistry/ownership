from ownership import server
from ownership.models import Owners
import unittest
import json
import mock
import uuid


#Set up test models
test_owner1 = Owners()
test_owner1.lrid = 'a8098c1a-f86e-11da-bd1a-00112444be1e'
test_owner1.owner_index = 1

test_owner2 = Owners()
test_owner2.lrid = 'd7cd9904-2f84-11e4-b2e1-0800277f1059'
test_owner2.owner_index = 2

test_owners = [test_owner1, test_owner2]




class OwnershipTestCase(unittest.TestCase):

    def setUp(self):
        server.app.config['TESTING'] = True
        self.app = server.app.test_client()

    def test_server(self):
        response = self.app.get('/')
        assert response.status == '200 OK'

    @mock.patch('ownership.server._find_owners', return_value=test_owners)
    def test_get_owners(self, mock_find):
        data = json.dumps({"title_number":"DN100"})
        response = self.app.post('/owners', data=data, content_type='application/json')
        assert response.data == '{"owners": [{"index": 1, "lrid": "a8098c1a-f86e-11da-bd1a-00112444be1e"}, {"index": 2, "lrid": "d7cd9904-2f84-11e4-b2e1-0800277f1059"}]}'
        assert response.status == '200 OK'

    @mock.patch('ownership.server._find_owners', return_value=[])
    def test_no_owner_found(self, mock_find):
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

    def test_health(self):
        response = self.app.get('/health')
        self.assertEqual(response.status, '200 OK')
