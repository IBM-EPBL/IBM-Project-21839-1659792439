from flask_login import UserMixin
from __init__ import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    
    
class Expenses(db.Model):
    #USERID,DATE,EXPENSENAME,AMOUNT,PAYMENTMODE,CATEGORY,TIME
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    date = db.Column(db.String(100))
    Expensename = db.Column(db.String(100))
    amount=db.Column(db.Integer())
    paymentmode=db.Column(db.String(100))
    category =db.Column(db.String(100))
    time=db.Column(db.String(100))
    
#     def __init__(self,user_id,date,Expensename,amount,paymentmode,category, time):
#         self.user_id=user_id
#         self.date=date
#         self.Expensename=Expensename
#         self.amount=amount
#         self.paymentmode=paymentmode
#         self.category=category
#         self.time=time
    