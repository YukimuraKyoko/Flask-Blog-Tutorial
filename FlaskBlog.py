from flask import Flask, render_template
app = Flask(__name__)

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
	
	

#Automatically turns debug on
#With this you can use "python FlaskBlog.py" instead of "flask run"
if __name__ == '__main__':
	app.run(debug=True)