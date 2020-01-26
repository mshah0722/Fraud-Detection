from sklearn import svm
import json

FILE = "./response_1579986544708.json"


def location_price_model(json_trans_data):
    x = []
    y = []

    with open(json_trans_data, 'r') as f:
        array = json.load(f)

    for i in array['result']:
        price = float(i['currencyAmount'])

        if price > 0 and "locationLongitude" in i:
            loc_lat = float(i['locationLatitude'])
            loc_long = float(i['locationLongitude'])

            x.append([loc_lat, loc_long])
            y.append(price)

    clf = svm.SVR()
    clf.fit(x, y)

    return clf
