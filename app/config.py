import os

currdir = os.path.dirname(os.path.realpath(__file__))

class Config(object):
	SECRET_KEY = "this is secret key from de4rm"
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(currdir,"bd.sqlite")
	SQLALCHEMY_TRACK_MODIFICATIONS = False