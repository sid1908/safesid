from flask import Flask, render_template, request, redirect, url_for
from models1 import *
import pandas as pd
app = Flask(__name__)

@app.route('/')
def create_data():
	col_names = ['DEVICE_NAME', 'DEVICE_TYPE', 'HASHTAGS']
	data =  pd.read_csv('db.csv', delimiter = ';', names = col_names)
	return str(data.loc[:,['DEVICE_NAME']])

if __name__ == '__main__':
    app.run(debug=True)
    
