from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired
from app.utils.list_images import list_images


class HistogramForm(FlaskForm):
    """
    A form class that extends FlaskForm and provides an alternative to web forms.
    It implements the fields in the template and handles the return data in the application.
    WTForms also uses a CSRF token to provide protection against CSRF attacks.
    """

    image = SelectField('Image', choices=list_images(), validators=[DataRequired()])
    submit = SubmitField('Submit')
