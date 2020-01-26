from prediction_models import get_cat_and_loc_model
import pickle
import json
from sklearn import svm
from td-api import get_all_customer_data, get_transations_by_customer

import requests

X = []
Y = []

for c in get_all_customer_data()[:300]:

    transations = get_transations_by_customer(c['id'])
    print("customer", c['id'])
    for t in transations:
        print("transaction", t['id'])
        price = float(t['currencyAmount'])
        if price > 0 and "merchantCategoryCode" in t and "locationLongitude" in t:
            merchantCatCode = int(t['merchantCategoryCode'])
            loc_long = float(t['locationLongitude'])
            loc_lat = float(t['locationLatitude'])

            X.append([merchantCatCode, loc_long, loc_lat])
            Y.append(price)

print("creating model")
clf = svm.SVR()
print("finished creating model")

print("training model")
clf.fit(X, Y)
print("finished training model")

pickle.dump(clf, open("mass-population-category-and-location.model", "wb"))
