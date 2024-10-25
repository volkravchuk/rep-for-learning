from flask import render_template 
from application import app

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/calculate')
# def calculate():
#     calc_instance = Calculate(2, "/", 3)
#     return render_template('index.html', calc_instance = calc_instance)