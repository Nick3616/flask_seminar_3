from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from model import User, RegistrationForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SECRET_KEY'] = b'174fe60e14c7d16a54c6dff81e38ad05'
csrf = CSRFProtect(app)
db = SQLAlchemy(app)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate():
        new_user = User(name=form.name.data, lastname=form.lastname.data, email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
    return render_template('form.html', form=form)

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')

if __name__ == "__main__":
    app.run(debug=True)