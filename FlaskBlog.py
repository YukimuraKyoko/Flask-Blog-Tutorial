from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return "Home"
	
@app.route("/about")
def about():
	return "About"
	
	

#Automatically turns debug on
#With this you can use "python FlaskBlog.py" instead of "flask run"
if __name__ == '__main__':
	app.run(debug=True)