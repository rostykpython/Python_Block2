from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, FieldList, TextAreaField, FormField
from wtforms.validators import DataRequired


class TagForm(FlaskForm):
    tag = StringField('tag')


class AddressBookForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    phone = StringField('phone', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    birthday = DateField('birthday', validators=[DataRequired()])
    street = StringField('street', validators=[DataRequired()])
    submit = SubmitField('Insert data')


class NoteForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    note = TextAreaField('Note', validators=[DataRequired()])
    # tags = StringField('Tags', validators=[DataRequired()])
    tags = FieldList(FormField(TagForm), min_entries=3)
    submit = SubmitField('Save')


