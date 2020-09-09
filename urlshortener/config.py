import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	"""Конфиг проекта"""

	DEBUG = True
	SECRET_KEY = 'djhnjp98735p92br389b7r9np92n8y3qm4d34y83m4np9843qd4sgqo32y83f4]'
	
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
