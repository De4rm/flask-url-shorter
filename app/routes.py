import validators
from socket import gethostname
from flask import render_template, redirect, abort
from app import app
from app.forms import ShortForm
from app.models import Link, check_if_exist, create_new_record

address = "http://127.0.0.1:5000"

@app.route("/", methods=["GET","POST"])
def index():
	form = ShortForm()
	error = ""
	if form.validate_on_submit():
		submited_url = form.url.data
		if validators.url(submited_url):
			result = check_if_exist(submited_url)
			if result == None:
				generated_url = create_new_record(submited_url)
			else:
				generated_url = result.url_generated

			form.url.data = address + "/" + generated_url
		else:
			error = "* url is not valid."

	return render_template('index.html',form=form, error=error)

@app.route('/<string:gen_url>')
def access_site(gen_url):
	result = check_if_exist(gen_url, True)
	if result == None:
		abort(404)
	return redirect(result.url_user)