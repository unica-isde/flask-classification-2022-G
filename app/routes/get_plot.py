from flask import Response, abort
import json
from app import app
from app.utils import json_data, custom_plot

@app.route('/plot/<string:job_id>', methods=['GET'])
def get_plot(job_id):
    """
    Return plotted data as a PNG file.
    """
    content = json_data.fetch(job_id)
    if content is None:
        abort(404)
    else:
        data_dict = json.loads(content)
        labels, values = zip(*data_dict.items())
        img = custom_plot.generate(labels, values)
        headers = {'Content-Disposition': 'attachment;filename=plot.png'}
        return Response(img, mimetype='image/png', headers=headers)
