from flask import Flask, request, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import hashlib

import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(16)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    token_hash = db.Column(db.String(64), unique=True, nullable=False)

    def __repr__(self):
        return f'<User id:{self.id}, name:{self.username}>'


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    user_id = session.get('user_id')
    user_name = session.get('user_name')
    return render_template('home.html', user_id=user_id, user_name=user_name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        token = request.form['token']
        token_hash = hashlib.sha256(token.encode()).hexdigest()

        user = User.query.filter_by(token_hash=token_hash).first()
        if user:
            session['user_id'] = user.id
            session['user_name'] = user.username
            return redirect(url_for('home'))
        else:
            return "Invalid token"

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        new_token = request.form['new_token']
        token_hash = hashlib.sha256(new_token.encode()).hexdigest()

        # Check if the token already exists
        existing_user = User.query.filter_by(token_hash=token_hash).first()
        if existing_user:
            return render_template('register.html', error="Token already in use. Please choose another.")

        new_user = User(username=username, token_hash=token_hash)
        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.id
        session['user_name'] = new_user.username
        return redirect(url_for('home', message='registered'))

    return render_template('register.html')


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
