from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import URL, DataRequired


class URLForm(FlaskForm):
	""" Форма """
	
	url_string = StringField('URL', validators=[DataRequired(), URL(message='Invalid URL!')])
	submit = SubmitField('Shorten')
