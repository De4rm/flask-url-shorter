from flask import render_template
from app import app
from app.forms import ShortForm

@app.route("/", methods=["GET","POST"])
def index():
	form = ShortForm()
	if form.validate_on_submit():
		pass
	return render_template('index.html',form=form)