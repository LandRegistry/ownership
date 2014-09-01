from ownership import app
from ownership.models import Owners
from flask import request, Response
from flask_negotiate import consumes
import json

@app.route('/')
def index():
    return "OK"

@app.route('/owners', methods=['POST', 'GET'])
@consumes('application/json')
def owners():
    if request.method == 'POST':

        title_number = request.json.get("title_number")

        if title_number:
            title_owners = _find_owners(title_number=title_number)

            data = {"owners":[]}

            if title_owners:
              for owner in title_owners:
                owner_dict = {"index" : owner.owner_index, "lrid" : str(owner.lrid)}
                data["owners"].append(owner_dict)

            app.logger.info("repsonse: %s" % (json.dumps(data)))

            response = Response(response=json.dumps(data),
                    status=200,
                    mimetype="application/json")

            return response
        else:
            return Response("title_number field not found", status=400)

def _find_owners(title_number):
    title_owners = Owners.query.filter_by(title_number=title_number)
    return title_owners
