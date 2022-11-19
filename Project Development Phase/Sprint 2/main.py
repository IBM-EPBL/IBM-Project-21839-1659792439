from flask import Blueprint, render_template, flash,redirect,request,session
from flask_login import login_required, current_user
from __init__ import create_app, db
import ibm_db
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from models import User , Expenses

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
    date = request.form['date']
    expensename = request.form['expensename']
    amount = request.form['amount']
    paymode = request.form['paymode']
    category = request.form['category']
    time=request.form['time']
    object = Expenses(user_id=current_user.id,date=date,Expensename=expensename,amount=amount,paymentmode=paymode,category=category,time=time)
    db.session.add(object)
    db.session.commit()
    limit=5
    if(limit>10): 
        mail_from = 'muthusubramanian1008@gmail.com'
        mail_to = session['email']

        msg = MIMEMultipart()
        msg['From'] = mail_from
        msg['To'] = mail_to
        msg['Subject'] = 'Expense Alert Limit'
        mail_body = """
        Dear User, You have exceeded the specified monthly expense Limit!!!!

        """
        msg.attach(MIMEText(mail_body))

        try:
            server = smtplib.SMTP_SSL('smtp.sendgrid.net', 465)
            server.ehlo()
            server.login('apikey', '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')
            server.sendmail(mail_from, mail_to, msg.as_string())
            server.close()
            print("mail sent")
        except:
            print("issue")

    
    return redirect("/history")

@main.route("/limit")
@login_required
def limit():
       return redirect('/limitn')

@main.route("/limitnum" , methods = ['POST' ])
def limitnum():
     if request.method == "POST":
         number= request.form['number']

         return redirect('/limitn')
     
         
@main.route("/limitn") 
def limitn():
    row = 100000

    return render_template("limit.html" , y= row)

@main.route('/history')
@login_required
def history():
        object = Expenses.query.filter_by(user_id=current_user.id).all()
        food = 0
        Entertainment = 0
        Business = 0
        Rent = 0
        EMI= 0
        other = 0
        total = 0
      
        for i in object:
            if i.category == 'food':
               food = food + i.amount
            if i.category == 'entertainment':
               Entertainment = Entertainment + i.amount
            if i.category == 'EMI':
               EMI = EMI + i.amount
            if i.category == 'rent':
               Rent = Rent + i.amount
            if i.category == 'other':
               other = other + i.amount
            if i.category == 'business':
               Business = Business + i.amount
        
        total = food+Entertainment+Business+Rent+EMI+other
      
        return render_template('history.html',total=total,food=food,Entertainment=Entertainment,Business=Business,Rent=Rent,EMI=EMI,other=other)
  
@main.route('/report')
@login_required
def report(): 
        object = Expenses.query.filter_by(user_id=current_user.id).all()
        food = 0
        Entertainment = 0
        Business = 0
        Rent = 0
        EMI= 0
        other = 0
        total = 0
      
        for i in object:
            if i.category == 'food':
               food = food + i.amount
            if i.category == 'entertainment':
               Entertainment = Entertainment + i.amount
            if i.category == 'EMI':
               EMI = EMI + i.amount
            if i.category == 'rent':
               Rent = Rent + i.amount
            if i.category == 'other':
               other = other + i.amount
            if i.category == 'business':
               Business = Business + i.amount
        
        total = food+Entertainment+Business+Rent+EMI+other
      
        return render_template('report.html',total=total,food=food,Entertainment=Entertainment,Business=Business,Rent=Rent,EMI=EMI,other=other)

app = create_app() # we initialize our flask app using the __init__.py function

if __name__ == '__main__':
    db.create_all(app=create_app()) # create the SQLite database
    app.run(debug=True) # run the flask app on debug mode