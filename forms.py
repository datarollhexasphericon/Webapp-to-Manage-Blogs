from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    name = StringField('Username', validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class CommentForm(FlaskForm):
    body = CKEditorField("Write your comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")

class ContactForm(FlaskForm):
    name = StringField('Username', validators=[DataRequired()])
    email = StringField("E-mail address", validators=[DataRequired()])
    phone = StringField("Phone number", validators=[DataRequired()])
    body = CKEditorField("Your message here", validators=[DataRequired()])
    submit = SubmitField("Send message")