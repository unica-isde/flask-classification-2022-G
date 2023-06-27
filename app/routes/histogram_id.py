import redis
from rq import Connection, Queue
from app import app
from config import Configuration

config = Configuration()

@app.route('/histogram/<string:job_id>', methods=['GET'])
def histogram_id(job_id):
    """
    From the ID specified in the path, returns the status and the result of the identified job.
    """
    redis_url = Configuration.REDIS_URL
    redis_conn = redis.from_url(redis_url)
    with Connection(redis_conn):
        q = Queue(name=Configuration.QUEUE_HIST)
        task = q.fetch_job(job_id)

    response = {
        'task_status': task.get_status(),
        'data': task.result,
    }
    return response
