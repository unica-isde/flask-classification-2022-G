from app import app
from flask import Response, abort
from app.utils import json_data

@staticmethod
@app.route('/json/<string:job_id>', methods=['GET'])
def get_json(job_id):
    """Return JSON data as a file """
    data = json_data.fetch(job_id)
    if data is None:
        abort(404)
    else:
        return Response(data,
                        mimetype='application/json',
                        headers={'Content-Disposition': 'attachment;filename=data.json'})
