import re
from datetime import datetime

from sqlalchemy.orm import validates

from . import db
from .constants import MAIN_URL, RE_LEGAL_CAHRS
from .error_handlers import InvalidAPIUsage


class URLMap(db.Model):
    """ Модель для связи оригинальной и короткой ссылок. """
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String, nullable=False)
    short = db.Column(db.String(16), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(url):
        """ Метод для приведения полей модели к базовым структурам Python. """
        return dict(
            url = url.original,
            short_link = MAIN_URL + url.short
        )
    
    def from_dict(self, data):
        """ Метод для приведения данных из запроса к необохдимому типу. """
        for field in ['original', 'short']:
            if field in data:
                setattr(self, field, data[field])

    @validates('original')
    def validate_original(self, key, value):
        if not value:
            raise InvalidAPIUsage('\"url\" является обязательным полем!')
        return value
    
    @validates('short')
    def validate_short(self, key, value):
        if URLMap.query.filter_by(short=value).first():
            raise InvalidAPIUsage(
                'Предложенный вариант короткой ссылки уже существует.'
                )

        correct = re.match(RE_LEGAL_CAHRS, value)
        if not correct:
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки'
                )
        return value
