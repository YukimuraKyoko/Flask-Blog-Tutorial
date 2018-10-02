from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisterationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'ceca7ffa42e3d3b78e6ca32add09c505'

posts =[
	{
		'author': 'Person1',
		'title': 'post1',
		'content': 'First content',
		'date_posted': 'date1'
	
	},
	{
		'author': 'Person2',
		'title': 'post2',
		'content': '2nd content',
		'date_posted': 'date2'
	
	}


]

@app.route("/")
@app.route("/home")
def home():
	return render_template('index.html', posts=posts)
	
@app.route("/about")
def about():
	return render_template('about.html', title='About')
	
@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegisterationForm()
	if form.validate_on_submit():
		flash('Account created!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)	

#Automatically turns debug on
#With this you can use "python FlaskBlog.py" instead of "flask run"
if __name__ == '__main__':
	app.run(debug=True)