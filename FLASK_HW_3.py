from flask import Flask, request, render_template
from MODELS_HW_3 import Users, db
from FORMS_HW_3 import RegisterForm
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SECRET_KEY'] = b'sdkvhag43j2btrmwvjuyg2u3'
csrf = CSRFProtect(app)
db.init_app(app)


@app.route('/db-hw-init/')
def init_db():
    db.create_all()
    print('OK')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    reg = RegisterForm()
    if request.method == 'POST' and reg.validate():
        first_name = reg.first_name.data
        last_name = reg.last_name.data
        password = reg.password.data
        email = reg.email.data
        users = Users(first_name=first_name, last_name=last_name, password_hash=password, email=email)
        db.session.add(users)
        db.session.commit()
    return render_template('register.html', form=reg)


if __name__ == '__main__':
    app.run()
    init_db()

