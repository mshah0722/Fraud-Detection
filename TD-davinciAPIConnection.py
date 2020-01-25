# install the requests package using 'python -m pip install requests'
import requests

response1 = requests.post(
    'https://api.td-davinci.com/api/raw-customer-data-csv',
    headers = { 'Authorization': 'YOUR API KEY GOES HERE' },
    json={ 'continuationToken': '' }
)
responseJson = response1.json()['result']
continuationToken = responseJson['continuationToken']
csvLines = responseJson['customersCsv']

response2 = requests.post(
    'https://api.td-davinci.com/api/raw-customer-data-csv',
    headers = { 'Authorization': 'YOUR API KEY GOES HERE' },
    json={ 'continuationToken': continuationToken }
)
csvLines += response2.json()['result']['customersCsv'] 

# # Example 1 - read API CSV data into pandas
# import sys
# import pandas as pd
# if sys.version_info[0] < 3: 
#     from StringIO import StringIO
# else:
#     from io import StringIO
# TESTDATA = StringIO(csvLines)
# df = pd.read_csv(TESTDATA, keep_default_na=False)
# print(df)

# # Example 2 - simple API CSV data
# import csv
# csvData = csv.DictReader(csvLines.splitlines())
# for row in csvData:
#    print(row['id'], row['age'])
