from flask_wtf import Form
from wtforms import StringField, BooleanField, SelectField, FileField
from wtforms.validators import DataRequired


class LoginForm(Form):
    input_data = FileField(u'input_data')#, [validators.regexp(u'^[^/\\]\.jpg$')])
    first_layer = SelectField(u'first_layer', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
