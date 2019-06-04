from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
from flask_pagedown.fields import PageDownField


class ProfileForm(FlaskForm):
    nickname = StringField('nickname', validators=[Length(0, 7)])
    about_me = PageDownField('about me', validators=[Length(0, 140)])

class PostForm(FlaskForm):
    body = TextAreaField('Post', validators=[DataRequired()])
    title = StringField('Title', validators=[Length(1, 20)])
    save_draft = SubmitField('Submit')
    submit = SubmitField('Publish')

class EditpostForm(FlaskForm):
    title = StringField('Title', validators=[Length(1, 20)])
    body = TextAreaField('Post', validators=[DataRequired()])
    update = SubmitField('Update')
    submit = SubmitField('Submit')
    save_draft = SubmitField('Submit')

class CommentForm(FlaskForm):
    body = PageDownField('Comment', validators=[DataRequired()])

class ReplyForm(FlaskForm):
    body = PageDownField('Reply', validators=[DataRequired()])

class SearchForm(FlaskForm):
    search = StringField('Search', validators=[DataRequired()])
