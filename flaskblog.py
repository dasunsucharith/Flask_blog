from flask import Flask, redirect, render_template, url_for, flash  
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
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'sucharith.dasun@gmail.com' and form.password.data == 'dasun1993':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
