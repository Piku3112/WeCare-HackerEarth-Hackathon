from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class RegistrationForm(FlaskForm):
	username = StringField('Username',
							validators=[DataRequired(),Length(min=2,max=20)])
	phone = StringField('Phone',
							validators=[DataRequired(), Length(min=10,max=10)])
	email = StringField('Email',
							validators=[DataRequired(),Email()])
	password = PasswordField('Password',
							validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password',
							validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')





class LoginForm(FlaskForm):
	email = StringField('Email',
							validators=[DataRequired(),Email()])
	password = PasswordField('Password',
							validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

class ForgotForm(FlaskForm):
	email = StringField('Email',
							validators=[DataRequired(),Email()])
	submit = SubmitField('Send')

class ChangePasswordForm(FlaskForm):
	email = StringField('Email',
							validators=[DataRequired(),Email()])
	password = PasswordField('Password',
							validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password',
							validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Change Password')