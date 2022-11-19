from flask import Blueprint, render_template, flash,redirect,request,session
from flask_login import login_required, current_user
from __init__ import create_app, db
import ibm_db
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

main = Blueprint('main', __name__)

main.secret_key="secured"

@main.route('/') # home page that return 'index'
def index():
    return render_template('index.html')

@main.route('/dashboard') # profile page that return 'profile'
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.name)

@main.route('/addexpenses',methods=['GET', 'POST'])
@login_required
def addexpenses():
    return render_template('addexpenses.html')

@main.route("/limit")
@login_required
def limit():
    return render_template("limit.html")

@main.route('/history')
@login_required
def history():
      return render_template('history.html')
  
@main.route('/report')
@login_required
def report():
    return render_template("report.html")

app = create_app() # we initialize our flask app using the __init__.py function

if __name__ == '__main__':
    db.create_all(app=create_app()) # create the SQLite database
    app.run(debug=True) # run the flask app on debug mode