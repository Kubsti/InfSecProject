from flask_wtf import FlaskForm
import flask_wtf as wtf
from wtforms import StringField,PasswordField,SubmitField, TextAreaField
from wtforms.validators import DataRequired,Length,EqualTo,Email

class RegistrationForm(FlaskForm):
    username = StringField(label='Username',validators=[DataRequired(),Length(min=3,max=20)])
    email = StringField(label='Email',validators=[DataRequired(),Email()])
    password = PasswordField(label='Password',validators=[DataRequired(),Length(min=6,max=16)])
    confirm_password = PasswordField(label='Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField(label='Sign Up')

class LoginForm(FlaskForm):
    email = StringField(label='Email',validators=[DataRequired(),Email()])
    password = PasswordField(label='Password',validators=[DataRequired(),Length(min=6,max=16)])
    submit=SubmitField(label='Log in')   

class CreatePostForm(FlaskForm):
    posttitel = StringField(label='Posttitel',validators=[DataRequired()])
    postcontent = TextAreaField(label='Postcontent',validators=[DataRequired()])
    submit=SubmitField(label='Create Post')

class CreateCommentForm(FlaskForm):
    commentcontent = TextAreaField(label='',validators=[DataRequired()])
    submit=SubmitField(label='Create Comment')
    