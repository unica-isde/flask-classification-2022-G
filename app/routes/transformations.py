from flask import render_template

from app import app
from app.forms.transformation_form import TransformationForm
from config import Configuration
import os
from PIL import Image, ImageEnhance

config = Configuration()

@app.route('/transformations', methods=['GET', 'POST'])
def transformations():
    form = TransformationForm()

    image_path = get_path()

    if form.validate_on_submit():  # POST
        # get transformation(s) data from the form in float type
        color = float(form.color.data)
        brightness = float(form.brightness.data)
        contrast = float(form.contrast.data)
        sharpness = float(form.sharpness.data)
        
        image_id = form.image.data

        # transforming image using the form's parameters with the subsidiary function
        mod_image_id = apply_transform(image_path, image_id, color, brightness, contrast, sharpness)

        # returns the transformed image alongside the original one
        return render_template("transformation_output.html", original_image_id=image_id, new_image_id=mod_image_id)

    # otherwise, it is a get request and should return the
    # image and transformations selector
    return render_template('transformation_select.html', form=form)


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
