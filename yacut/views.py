from random import choice
from string import ascii_lowercase, ascii_uppercase, digits

from flask import abort, flash, render_template, redirect, url_for

from . import app, db
from .constants import MAIN_URL
from .forms import URLMapForm
from .models import URLMap
from .utils import generate_url


@app.route('/', methods=['GET', 'POST'])
def generate_short_id_view():
    """ Viev-функция для генерации короткой ссылки. """
    form = URLMapForm()
    if form.validate_on_submit():
        short = form.custom_id.data
        original = form.original_link.data
        if not short:
            short = generate_url()
        elif URLMap.query.filter_by(short=short).first():
                flash('Предложенный вариант короткой ссылки уже существует.')
                return render_template('index.html', form=form)
        url_map = URLMap(
             original = original,
             short = short
        )
        db.session.add(url_map)
        db.session.commit()
        context = {'url_map': url_map, 'form': form, 'main_url': MAIN_URL}
        return render_template('index.html', **context)
    return render_template('index.html', form=form)


@app.route('/<string:short>')
def short_id_view(short):
    """ View-функция для переадресации с короткой ссылки на оригинальную. """
    url_map = URLMap.query.filter_by(short=short).first()
    if not url_map:
        abort(404)
    return redirect(url_map.original)
