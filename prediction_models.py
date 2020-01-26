from sklearn import svm
import json
import pickle
import random

FILE = "./response_1579986544708.json"


def get_list(json_file):
    with open(json_file, 'r') as f:
        array = json.load(f)

    return array['result']


def parse_data_into_X_and_Y(data_list):
    X = []
    Y = []

    for i in data_list:
        price = float(i['currencyAmount'])

        if price > 0 and "merchantCategoryCode" in i and "locationLongitude" in i:
            merchantCatCode = int(i['merchantCategoryCode'])
            loc_long = float(i['locationLongitude'])
            loc_lat = float(i['locationLatitude'])


            

            X.append([merchantCatCode, loc_long, loc_lat])
            Y.append(price)

    return X, Y


def parse_data_into_categories_to_data(X, Y):
    categories_to_data = {}

    long_list = []
    lat_list = []

    for i, x in enumerate(X):
        long_list.append(x[1])
        lat_list.append(x[2])
        if x[0] in categories_to_data:
            categories_to_data[x[0]]['X'].append(
                [x[1], x[2]])
            categories_to_data[x[0]]["Y"].append(
                Y[i]
            )
        else:
            categories_to_data[x[0]] = {"X": [], "Y": []}
            categories_to_data[x[0]]['X'].append(
                [x[1], x[2]])
            categories_to_data[x[0]]["Y"].append(
                Y[i]
            )

            # X.append([merchantCatCode, loc_long, loc_lat])
            # Y.append(price)

    return categories_to_data, long_list, lat_list


def train(cat_to_data):
    category_to_model = {}

    multiplier = 1

    for cat in cat_to_data:

        X = cat_to_data[cat]["X"]
        Y = cat_to_data[cat]["Y"]

        clf = svm.SVR()
        clf.fit(X, Y)

        category_to_model[cat] = clf

    return category_to_model



# list_data = get_list(FILE)

# parsed = parse_data(list_data)

# train(parsed)
# list_data = get_list(FILE)
# X, Y, long_list, lat_list = parse_data_into_X_and_Y(list_data)
# train_data_X = X[:134]
# train_data_Y = Y[:134]
# test_data_X = X[135:]
# test_data_Y = Y[135:]

# parsed = parse_data_into_categories_to_data(train_data_X, train_data_Y)

# cat_to_model = train(parsed)


def test_model():
    list_data = get_list(FILE)
    X, Y = get_cat_and_loc_alone_in_train_and_test_data(list_data)

    train_data_X = X[:134]
    train_data_Y = Y[:134]

    test_data_X = X[135:]
    test_data_Y = Y[135:]

    parsed = parse_data(train_data_X, train_data_Y)

    cat_to_model = train(parsed)

    total = len(test_data_X)
    success = 0
    no_model_of_cat = 0

    for i, x in enumerate(test_data_X):

        if x[0] not in cat_to_model:
            no_model_of_cat += 1
            pass

        result = cat_to_model[x[0]].predict([[x[1], x[2]]])[0]

        acceptance_range = 1.3
        final_result = result * acceptance_range
        # or (result * acceptance_range) <= test_data_Y[i]:
        if (final_result) >= test_data_Y[i] or ((final_result < test_data_Y[i]) and ((test_data_Y[i] - final_result) <= 4)):
            success += 1
        else:
            print(final_result, test_data_Y[i], x[0])

    print("accuracy:", (success / total))
    print("success:", success, "total:", total,
          "not model of category:", no_model_of_cat)


# test_model()

# def test_model():
#  X = []
#   Y = []

#    with open(FILE, 'r') as f:
#         array = json.load(f)
#     # random.shuffle(array)

#     for i in array['result']:
#         price = float(i['currencyAmount'])

#         if price > 0 and "merchantCategoryCode" in i:
#             merchantCatCode = int(i['merchantCategoryCode'])

#             X.append([merchantCatCode])
#             Y.append(price)

#     train_data_X = X[:int((len(X)/2))]
#     train_data_Y = Y[:int((len(Y)/2))]

#     test_data_X = X[(int(len(X)/2)):]
#     test_data_Y = Y[(int(len(Y)/2)):]

#     clf = svm.SVR()

#     clf.fit(train_data_X, train_data_Y)

#     total_trials = len(test_data_X)
#     total_success = 0

#     for i, x in enumerate(test_data_X):
#         result = clf.predict([x])[0]

#         if (result * 2) >= test_data_Y[i]:
#             # print(result*2, test_data_Y[i])
#             total_success += 1
#         else:
#             print(result*2, test_data_Y[i], x[0])
#     print(total_success, total_trials)
#     print("accuracy:", total_success/total_trials)

# model = get_cat_and_loc_model(FILE)

# pickle.dump(model, open("get_loc_and_model.model", "wb"))

# cat, loc
# mass population on cat and loc
# fruqency - online // physical // if possible
