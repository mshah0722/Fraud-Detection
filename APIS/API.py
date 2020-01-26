# install the requests package using 'python -m pip install requests'
import requests

response1 = requests.post(
    'https://api.td-davinci.com/api/raw-customer-data',
    headers = { 'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDQlAiLCJ0ZWFtX2lkIjoiODllZjBiNGYtMGU4Zi0zMmZkLThjYWEtNTFjOTdkYWFjYzgwIiwiZXhwIjo5MjIzMzcyMDM2ODU0Nzc1LCJhcHBfaWQiOiI3ZDFmNzUzNi02M2Q0LTRjZTgtYmVmZi0xOWU5ZjYxMjA3MmYifQ.V1IDoKZ25qke-lZlu8uBX95TWuyfTFfu1AGqu6X7TWI' },
    json={ 'continuationToken': '' }
)
responseJson = response1.json()['result']
continuationToken = responseJson['continuationToken']

# response2 = requests.post(
#     'https://api.td-davinci.com/api/raw-customer-data',
#     headers = { 'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDQlAiLCJ0ZWFtX2lkIjoiODllZjBiNGYtMGU4Zi0zMmZkLThjYWEtNTFjOTdkYWFjYzgwIiwiZXhwIjo5MjIzMzcyMDM2ODU0Nzc1LCJhcHBfaWQiOiI3ZDFmNzUzNi02M2Q0LTRjZTgtYmVmZi0xOWU5ZjYxMjA3MmYifQ.V1IDoKZ25qke-lZlu8uBX95TWuyfTFfu1AGqu6X7TWI' },
#     json={ 'continuationToken': continuationToken }
# )
# csvLines += response2.json()['result']['customers'] 



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
