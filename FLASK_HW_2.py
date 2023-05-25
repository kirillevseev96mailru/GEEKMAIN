from flask import Flask, render_template, request, url_for, redirect
from pathlib import PurePath, Path
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('FLASK_HW_2_1.html')


@app.route('/registr/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        context = {}
        context.update(name=username, email=email)
        return render_template('Flask_HW_2_3.html', **context)
    return render_template('Flask_HW_2_2.html')


@app.route('/hello/', methods=['GET', 'POST'])
def hello():
    return render_template('Flask_HW_2_3.html')


if __name__ == '__main__':
    app.run()