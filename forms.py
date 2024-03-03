from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, URL, NumberRange, Optional

class PetForm(FlaskForm):
    """Form for creating new pets and editing information for existing ones"""
    name = StringField('Name', validators=[InputRequired()])
    species = SelectField('Species', choices=[('dog','Dog'), ('cat','Cat'), ('porucpine','Porcupine')], validators=[InputRequired()])
    photo_url = StringField('Photo URL', validators=[URL(require_tld=False, message = 'This is not a valid URL'), Optional()])
    age = IntegerField('Age', validators=[NumberRange(min = 0, max = 30, message = 'Age must be between 0 and 30')])
    notes = StringField('Notes')
    available = BooleanField('Availability', validators=[InputRequired()])

    