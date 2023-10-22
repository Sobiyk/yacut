from random import choice

from .constants import LEGAL_CHARS, GENERATED_SHORT_ID_LENGTH
from .models import URLMap


def string_generator():
    """ Функция для генерации короткой ссылки. """
    return ''.join(choice(LEGAL_CHARS) for _ in range(
        GENERATED_SHORT_ID_LENGTH))


def generate_url():
    """ Функция генерирующая короткую ссылку пока она не станет уникальной. """
    short = string_generator()
    while URLMap.query.filter_by(short=short).first():
        short = string_generator()

    return short
