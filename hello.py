from flask import Flask, render_template


# Create A Flask Instance
app = Flask(__name__)

# Create a route decerator
@app.route('/')

#def index():
	#return "<h1>Hello World!</h1>"

def index():
	first_name = "Ihsaan"
	stuff = "This is bold text"

	favourite_pizza = ["Peperoni", "Cheese", "Mushroom", 41]
	return render_template("index.html",
		first_name=first_name,
		stuff=stuff,
		favourite_pizza = favourite_pizza)

# localhost:5000/user/Ihsaan
@app.route('/user/<name>')

def user(name):
	return render_template("user.html", user_name=name)

# Create Custom Error Pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
	return render_template("505.html"), 500			