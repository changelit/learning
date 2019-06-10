from flask import Flask, render_template, flash, url_for, request, redirect
from main import forms
import os
import uuid

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html', e=e), 404


@app.route('/flash')
def just_flash():
    flash('Current Version is too old')
    return '', 302, {'Location': '/'}


def random_filename(filename):
    ext = os.path.splitext(filename)[1]
    new_filename = uuid.uuid4().hex + ext
    return new_filename


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        f = form.photo.data
        filename = random_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        flash('Upload %s succesfully ' % filename)
        flash('Welcome you %s' % username)
        return redirect(url_for('just_flash'))
    return render_template('login.html', form=form)


app.config['UPLOAD_PATH'] = os.path.join(app.root_path, 'uploads')
app.jinja_env.lstrip_blocks = True
app.jinja_env.trim_blocks = True
app.secret_key = '123456'

if __name__ == '__main__':
    app.run()
