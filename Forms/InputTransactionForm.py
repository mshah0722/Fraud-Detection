from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, DateTimeField, IntegerField, SubmitField
from wtforms.validators import DataRequired, ValidationError

class TransactionForm(FlaskForm):
    customerID = StringField("CustomerID", validators = [DataRequired()])
    cost = DecimalField("Cost", validators = [DataRequired()])
    date = IntegerField("Date")
    time = IntegerField("Time")
    longitude = DecimalField("Longitude", validators = [DataRequired()])
    latitude = DecimalField("Latitude", validators = [DataRequired()])
    categoryID = IntegerField("CategoryID", validators = [DataRequired()])
    submit = SubmitField('Submit')
    