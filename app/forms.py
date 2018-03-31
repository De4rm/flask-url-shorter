from flask_wtf import FlaskForm
from wtform import StringField, SubmitField
from wtform.validators import DataRequired

class ShortForm(FlaskForm):
	url = StringField('URL', validators=[DataRequired()])
	submit = SubmitField('Shorten')
