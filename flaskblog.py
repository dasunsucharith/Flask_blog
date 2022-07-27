from turtle import title
from flask import Flask, render_template, url_for 
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '843eaa1491c7a4130988d7c3ee4a9f4c'

posts = [
    {
        'author': 'Dasun Sucharith',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'July 23, 2022'
    },
    {
        'author': 'Rebecca Rubasinghe',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'July 24, 2022'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
