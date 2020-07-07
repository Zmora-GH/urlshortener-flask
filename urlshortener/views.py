from flask import render_template, flash, redirect
from app import app
from forms import URLForm

@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLForm()
    if form.validate_on_submit():
        print(f'{form.url_string.data} --> in BD')
        return redirect('/')

    return render_template('index.html', form=form)
