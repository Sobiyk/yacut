from flask_wtf import FlaskForm
from wtforms import URLField, SubmitField, StringField
from wtforms.validators import DataRequired, Length, Optional


class URLMapForm(FlaskForm):
    """ Форма для генерации короткой ссылки. """
    original_link = URLField(
        'Введите оригинальную ссылку',
        validators=[DataRequired(message='Обязательное поле')])
    custom_id = StringField(
        'Введите свой вариант короткой ссылки',
        validators=[Length(0, 16), Optional()]
    )
    create = SubmitField('Создать')
