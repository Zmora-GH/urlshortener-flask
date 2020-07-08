from flask import render_template, redirect, url_for, abort, request
from app import app, db
from forms import URLForm
from models import ShortURL

import string
import random


def random_url(N=8):
    slug = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(N))
    if db.session.query(ShortURL).filter_by(short_url=slug).first():
        return random_url
    return slug


def get_urls(short_url):
    url = db.session.query(ShortURL).filter_by(short_url=short_url).first()
    if not url:
        abort(404)
    surl = ''.join(request.host_url.split('//',1)[1:]) + url.short_url
    furl = url.full_url
    clicks = url.clicks
    return surl, furl, clicks


@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLForm()
    if form.validate_on_submit():
        url = db.session.query(ShortURL).filter_by(full_url=form.url_string.data).first()
        if url:
            return redirect(url_for('short_page', short_url=url.short_url))
        else:
            new_url = ShortURL(full_url=form.url_string.data, short_url=random_url())
            db.session.add(new_url)
            db.session.commit()
            return redirect(url_for('short_page', short_url=new_url.short_url))
    return render_template('index.html', form=form)


@app.route('/<short_url>/clicks')
def clicks(short_url):
    surl, furl, clicks = get_urls(short_url)
    return render_template('clicks.html', surl=surl, furl=furl, clicks=clicks)
    form = ClickURLForm()



@app.route('/short/<short_url>')
def short_page(short_url):
    surl, furl, _ = get_urls(short_url)
    return render_template('short.html', surl=surl, furl=furl, short_url=short_url)


@app.route('/<short_url>')
def redirecter(short_url):
    url = db.session.query(ShortURL).filter_by(short_url=short_url).first()
    if url:
        url.clicks += 1
        db.session.commit()
        return redirect(url.full_url)
    else:
        abort(404)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('p404.html'), 404
