
from flask import Flask,render_template

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('finalterm.html')
@app.route('/hello')
def hello():
    return render_template('finalterm.html')

app.run()
