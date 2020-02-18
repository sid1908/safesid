from peewee import *
import datetime

db = SqliteDatabase('logreg.db')

class User(Model):
	id = PrimaryKeyField()
	username = CharField()
	password = TextField()

	class Meta:
		database = db

def initialize_db():
	db.connect()
	db.create_tables([User], safe=True)
