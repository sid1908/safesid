from flask import Flask, session, redirect, url_for, escape, request, render_template
from hashlib import md5
import signup
import csv

app = Flask(__name__)

@app.route('/')
def login(username,password):
    username= username
    password= password
    with open('logreg.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if (row[0] == (username.upper())):
                if (row[1] == (password.upper())):
                    q = row[2]
                    break
            else:
                print('not found')

    return 'success'
    
    
if __name__ == "__main__":
        app.debug = True
        app.run()
