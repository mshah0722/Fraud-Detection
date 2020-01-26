from prediction_models import get_cat_and_loc_model
import pickle
import json
from sklearn import svm

import requests

API_KEY = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDQlAiLCJ0ZWFtX2lkIjoiYTk1YTcwM2QtYzMzZS0zMjQzLThlMzAtMjk3YTcwZjEwNzU1IiwiZXhwIjo5MjIzMzcyMDM2ODU0Nzc1LCJhcHBfaWQiOiIyODA0ZmJjOS0wMjViLTRmZTgtODg2Mi1lNTM2ZDZhYWYyOWIifQ.mY0gqgaxkAaQRbvU-Id_WBHO9v6PnYVXmXaxmAnrJL0'


def get_transations_by_customer(id):
    response = requests.get(
        "https://api.td-davinci.com/api/customers/52f7af91-e89b-495b-9beb-d7b267b7344e/transactions",
        headers={'Authorization': API_KEY}
    )
    json_data = json.loads(response.text)
    return json_data["result"]


def get_all_customer_data():

    response = requests.post(
        'https://api.td-davinci.com/api/raw-customer-data',
        headers={'Authorization': API_KEY}
    )

    json_data = json.loads(response.text)
    return json_data['result']['customers']


print(get_transations_by_customer(get_all_customer_data()[0]['id'])[0])

X = []
Y = []

for c in get_all_customer_data():

    transations = get_transations_by_customer(c['id'])

    for t in transations[:300]:
        if price > 0 and "merchantCategoryCode" in t and "locationLongitude" in t:
            price = float(i['currencyAmount'])
            merchantCatCode = int(t['merchantCategoryCode'])
            loc_long = float(t['locationLongitude'])
            loc_lat = float(t['locationLatitude'])

            X.append([merchantCatCode, loc_long, loc_lat])
            Y.append(price)

clf = svm.SVR()
clf.fit(X, Y)

pickle.dump(model, open("mass-population-category-and-location.model", "wb"))
