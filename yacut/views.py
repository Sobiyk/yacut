from http import HTTPStatus

from flask import abort, flash, render_template, redirect

from . import app, db
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
            original=original,
            short=short
        )
        db.session.add(url_map)
        db.session.commit()
        context = {'url_map': url_map, 'form': form}
        return render_template('index.html', **context)
    return render_template('index.html', form=form)


@app.route('/<string:short>')
def short_id_view(short):
    """ View-функция для переадресации с короткой ссылки на оригинальную. """
    url_map = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(url_map.original)
