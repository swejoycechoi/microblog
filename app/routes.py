from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'swejoycechoi'}
    posts = [
        {
            'author': {'username': 'Hunter'},
            'body': 'Machine learning in 2024'
        },
        {
            'author': {'username': 'Pia'},
            'body': 'Generative vs General AI'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)