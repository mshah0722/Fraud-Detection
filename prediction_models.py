from sklearn import svm
import json

FILE = "./response_1579986544708.json"


def get_cat_and_loc_model(json_transaction_data):

    X = []
    Y = []

    with open(json_transaction_data, 'r') as f:
        array = json.load(f)

    for i in array['result']:
        price = float(i['currencyAmount'])

        if price > 0 and "merchantCategoryCode" in i and "locationLongitude" in i:
            merchantCatCode = int(i['merchantCategoryCode'])
            loc_long = float(i['locationLongitude'])
            loc_lat = float(i['locationLatitude'])

            X.append([merchantCatCode, loc_long, loc_lat])
            Y.append(price)

    clf = svm.SVR()

    clf.fit(X, Y)

    return clf


# cat, loc
# mass population on cat and loc
# fruqency - online // physical // if possible
