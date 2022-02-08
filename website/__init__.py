#will make website folder python package
#will allow us to import this folder into another file
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db  = SQLAlchemy()

def create_application():
	application = Flask(__name__) #__name__ represents name of file
	application.config['SECRET_KEY'] = 'alsdkfjasldkjf' #secret key should not be shared in prod
	# application.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:pwd@localhost/dbg_staging"
	application.config['SQLALCHEMY_DATABASE_URI']="postgresql://dbg_devtest:dbg_password@database-2.c9zekcxdkpeh.us-east-2.rds.amazonaws.com:5375/database_test"
	db.init_app(application)
	
	from .views import views #importing all views
	from .auth import auth #importing all auth functions

	application.register_blueprint(views,url_prefix='/')
	application.register_blueprint(auth,url_prefix='/')


	return application

