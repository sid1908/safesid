from flask import Flask, render_template, request, redirect, url_for
from peewee import *
import datetime

db = SqliteDatabase('posts.db')

class Post(Model):
	id = PrimaryKeyField()
	date = DateTimeField(default = datetime.datetime.now)
	title = CharField()
	text = TextField()

	class Meta:
		database = db

def initialize_db():
	db.connect()
	db.create_tables([Post], safe=True)

app = Flask(__name__)

@app.route('/') 
def home():
        # render the home page with the saved posts
        return render_template('tech.html', posts=Post.select().order_by(Post.date.desc()))

@app.before_request
def before_request():
	# create db if needed and connet
	initialize_db()

@app.teardown_request
def teardown_request(exception):
	# close the db connection
	db.close()

if __name__ == '__main__':
    app.debug = True
    app.run()
