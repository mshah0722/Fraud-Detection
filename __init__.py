import sys
sys.path.append("APIS/")
sys.path.append("Forms/")

import API
from Transactions import get_transaction_data
from InputTransactionForm import TransactionForm

from flask import Flask, render_template, url_for, flash, redirect, request, jsonify
from flask_mongoengine import Document, MongoEngine
from flask_mongoengine.wtf import model_form
from datetime import datetime



app = Flask(__name__)

app.config['SECRET_KEY'] = '032893044egjhd3209r834'
app.config["MONGO_URI"] = 'mongodb+srv://user1:deltahacks@deltahacks-4necq.mongodb.net/test?retryWrites=true&w=majority'
app.config['MONGODB_SETTINGS'] = {
    'db': 'DeltaHacks',
    'host': 'mongodb+srv://user1:deltahacks@deltahacks-4necq.mongodb.net/test?retryWrites=true&w=majority'
}
db = MongoEngine(app)
app.config.update(
    DEBUG=True,
)



class Transaction(db.Document):
    customerID = db.StringField(required=True)
    cost = db.DecimalField(required = True)
    date = db.IntField()
    time = db.IntField()
    longitude = db.DecimalField(required = True)
    latitude = db.DecimalField(required = True)
    categoryID = db.IntField(required = True)

    def __repr__(self):
        return f"Transaction('{self.customerID}','{self.cost}','{self.date}','{self.time}','{self.longitude}','{self.latitude}','{self.categoryID}')"
    def __str__(self):
        return f"Transaction('{self.customerID}','{self.cost}','{self.date}','{self.time}','{self.longitude}','{self.latitude}','{self.categoryID}')"

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/users')
def get_users():
    return API.responseJson

@app.route('/transaction/<customerID>', methods=['GET'])
def get_transactions(customerID):
     return get_transaction_data(customerID)
    
@app.route('/input-transaction', methods=['GET', 'POST'])
def input_transaction():
    form = TransactionForm()
    if form.validate_on_submit():
        
        transaction = Transaction(customerID = form.customerID.data, cost = form.cost.data, longitude = form.longitude.data, latitude = form.latitude.data, categoryID = form.categoryID.data)
        transaction.save()
        flash(f'Transaction Added!', 'success')
        return (redirect(url_for('input_transaction')))
    return render_template('form.html', form = form)
    
@app.route('/get_approved_transactions', methods=['GET'])
def approved_transactions():
    array1 = []
    array2 = []
    for transaction in Transaction.objects:
        array1.append([transaction['categoryID'], transaction['longitude'], transaction['latitude']])
        array2.append(transaction['cost'])
    print(array1)
    print (array2)
    return jsonify(Transaction.objects)

@app.route('/get_unapproved_transactions', methods=['GET'])
def unapproved_transactions():
    return


    
if __name__ == '__main__':
    app.run()
