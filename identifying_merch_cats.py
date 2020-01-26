import json

FILE = "./response_1579986544708.json"

with open(FILE, 'r') as f:
    array = json.load(f)

# x = []
# y = []

merchs = {}

for i in array['result']:

    if 'merchantCategoryCode' in i and i['currencyAmount'] > 0:
        merch_cat = int(i['merchantCategoryCode'])

        if merch_cat in merchs and i['merchantName'] not in merchs[merch_cat]:
            merchs[merch_cat].append(i['merchantName'])
        else:
            # try:
            merchs[merch_cat] = [i['merchantName']]
            # except:
            # print(i['id'])


print(merchs)
