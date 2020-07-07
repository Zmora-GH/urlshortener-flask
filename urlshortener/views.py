from flask import render_template, redirect, url_for, abort
from app import app, db
from forms import URLForm
from models import ShortURL


import string
import random

BASE_URL = 'localhost:5000/'

def random_url(N=7):
    slug = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(N))
    if db.session.query(ShortURL).filter_by(short_url=slug).first():
        return random_url
    return slug


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
    #short_url == '' if >>> index else == valid short_url
    if short_url:
        pass
    pass


@app.route('/short/<short_url>')
def short_page(short_url):
    url = db.session.query(ShortURL).filter_by(short_url=short_url).first()
    surl = BASE_URL + url.short_url
    furl = url.full_url
    return render_template('short.html', surl=surl, furl=furl, short_url=url.short_url)


@app.route('/<short_url>')
def redirecter(short_url):
    url = db.session.query(ShortURL).filter_by(short_url=short_url).first()
    if url:
        return redirect(url.full_url)
    else:
        abort(404)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('p404.html'), 404
