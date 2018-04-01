from flask import render_template
from app import app
from app.forms import ShortForm
from app.models import Link, check_if_exist

@app.route("/", methods=["GET","POST"])
def index():
	form = ShortForm()
	if form.validate_on_submit():
		submited_url = form.url.data
		result = check_if_exist(submited_url)
		if result == None:
			generated_url = create_new_record(submited_url)

	return render_template('index.html',form=form)