from flask import
Flask,render_template,request,redirect,url_for,Response,request,jsonify

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('table.html')

app.run()
