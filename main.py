# Imports the Flask wrapper
from flask import Flask

# Creates an instance of the flask server using *this* module as its unique identifier
app = Flask(__name__)

#This is a function decorator, it basically is a middleware that attaches the function hello to the flask gateway
@app.route("/")
def home():
	return "Hello world"


# Ridiculously simplistic running mechanism
if __name__ == "__main__":
	app.run()