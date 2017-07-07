from flask_wtf import Form 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, length

class SignupForm(Form):
	first_name = StringField('First name', validators=[DataRequired("Please enter your first name.")])
	last_name = StringField('Last name', validators=[DataRequired("Please enter your last name.")])
	email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
	username = StringField('Username' , validators=[DataRequired("Please enter a username.")])
	password = PasswordField('Password', validators=[DataRequired("Please enter a password."), length(min=6, message="Passwords must be at least 6 characters long.")])
	submit = SubmitField('Sign up')