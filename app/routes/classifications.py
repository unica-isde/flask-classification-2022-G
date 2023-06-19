import redis
from flask import render_template
from rq import Connection, Queue
from rq.job import Job

from app import app
from app.forms.classification_form import ClassificationForm
from ml.classification_utils import classify_image
from config import Configuration
import os
from PIL import Image, ImageEnhance

config = Configuration()

@app.route('/classifications', methods=['GET', 'POST'])
def classifications():
    """API for selecting a model and an image and running a 
    classification job. Returns the output scores from the 
    model."""
    form = ClassificationForm()

    image_path = get_path()

    if form.validate_on_submit():  # POST
        # get transformation(s) data from the form in float type
        color = float(form.color.data)
        brightness = float(form.brightness.data)
        contrast = float(form.contrast.data)
        sharpness = float(form.sharpness.data)
        
        image_id = form.image.data
        model_id = form.model.data

        redis_url = Configuration.REDIS_URL
        redis_conn = redis.from_url(redis_url)

        # transforming image using the form's parameters with the subsidiary function
        mod_image_id = apply_transform(image_path, image_id, color, brightness, contrast, sharpness)
        image_id = mod_image_id

        with Connection(redis_conn):
            q = Queue(name=Configuration.QUEUE)
            job = Job.create(classify_image, kwargs={
                "model_id": model_id,
                "img_id": image_id
            })
            task = q.enqueue_job(job)

        # returns the image classification output from the specified model
        # return render_template('classification_output.html', image_id=image_id, results=result_dict)
        return render_template("classification_output_queue.html", image_id=image_id, jobID=task.get_id())

    # otherwise, it is a get request and should return the
    # image and model selector
    return render_template('classification_select.html', form=form)

# subsidiary function made to get the "working" path
def get_path():
    project_root = os.path.dirname(os.path.dirname(__file__))
    working_path = os.path.join(project_root, 'static/imagenet_subset/')
    return working_path

# subsidiary function responsible for the image transformation(s)
def apply_transform(path, id, col, br, con, sh):
    img_new_id = 'mod_' + id    # new image id
    
    img = Image.open(path + id)
    img_new = img

    # apply one transformation at a time
    img_new = ImageEnhance.Color(img_new).enhance(col)
    img_new = ImageEnhance.Brightness(img_new).enhance(br)
    img_new = ImageEnhance.Contrast(img_new).enhance(con)
    img_new = ImageEnhance.Sharpness(img_new).enhance(sh)
    
    img_new.save(path + img_new_id)
    
    return img_new_id
