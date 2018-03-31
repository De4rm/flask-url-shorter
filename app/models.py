from app import db

class Link(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	url_user = db.Column(db.String(120), index=True, unique=True)
	url_generated = db.Column(db.String(8), index=True, unique=True)

	def _repr__(self):
		return "Link, {}".format(self.url_user)