from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm


@app.route('/')
@app.route('/index')
@app.route('/login', methods=['GET', 'POST'])
def index():
    user = {'nickname': 'Piyush'}
    posts = [{
        'author': {'nickname': 'John'},
        'body': 'Beautiful day in Portland!'
    },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)


def login():
    form = LoginForm()
    return render_template('login.html', title='sign in', form=form)
