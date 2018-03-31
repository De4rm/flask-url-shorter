from flask import render_template
from app import app

@app.route("/", methods=["GET","POST"])
def index():
	return "Hello"