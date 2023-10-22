from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import generate_url


@app.route('/api/id/', methods=['POST'])
def generate_short_url():
    """ View-функция api для генерации короткой ссылки. """
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('\"url\" является обязательным полем!')
    if (
        'custom_id' in data and
        data['custom_id'] != '' and
        data['custom_id'] is not None
    ):
        data['short'] = data['custom_id']
    else:
        data['short'] = generate_url()
    data['original'] = data['url']
    url_map = URLMap()
    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.to_dict()), 201


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original_url(short_id):
    """ View-функция для получения оригинальной ссылки по короткой. """
    url_map = URLMap.query.filter_by(short=short_id).first()
    if url_map is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify({'url': url_map.original}), 200
