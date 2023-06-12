from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, DecimalField
from wtforms.validators import DataRequired
from wtforms.widgets import NumberInput

from app.utils.list_images import list_images
from config import Configuration

conf = Configuration()


class ClassificationForm(FlaskForm):
    model = SelectField('model', choices=conf.models, validators=[DataRequired()])
    image = SelectField('image', choices=list_images(), validators=[DataRequired()])
    color = DecimalField(places=1, default=1, widget=NumberInput(step=0.1, min=0.0, max=3.0))
    brightness = DecimalField(places=1, default=1, widget=NumberInput(step=0.1, min=0.0, max=3.0))
    contrast = DecimalField(places=1, default=1, widget=NumberInput(step=0.1, min=0.0, max=3.0))
    sharpness = DecimalField(places=1, default=1, widget=NumberInput(step=0.1, min=0.0, max=3.0))
    submit = SubmitField('Submit')
