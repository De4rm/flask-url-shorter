import string
import random

from app import db


chars = string.ascii_uppercase + string.ascii_lowercase + string.digits


class Link(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	url_user = db.Column(db.String(120), index=True, unique=True)
	url_generated = db.Column(db.String(8), index=True, unique=True)

	def _repr__(self):
		return "Link, {}".format(self.url_user)



def check_if_exist(url, generated = False):
	query = db.session.query(Link)

	if generated:
		col = Link.url_generated
	else:
		col = Link.url_user

	result = query.filter( col ==  url).one_or_none()
	return result

def create_new_record(url):
	new_url = generate_new_url()
	new_record = Link(url_user = url, url_generated=new_url)
	db.session.add(new_record)
	db.session.commit()

	return new_url


def generate_new_url():
	result = ''.join([random.choice(chars) for i in range(8)])
	if check_if_exist(result) != None:
		result = generate_new_url()
	return result
