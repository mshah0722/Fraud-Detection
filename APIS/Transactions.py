import requests

def get_transaction_data(customerID):
    response1 = requests.get(
        'https://api.td-davinci.com/api/customers/8b33d5a1-1c8c-4fc8-ade8-d014f1f27ed6/transactions',
        headers = { 'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDQlAiLCJ0ZWFtX2lkIjoiODllZjBiNGYtMGU4Zi0zMmZkLThjYWEtNTFjOTdkYWFjYzgwIiwiZXhwIjo5MjIzMzcyMDM2ODU0Nzc1LCJhcHBfaWQiOiI3ZDFmNzUzNi02M2Q0LTRjZTgtYmVmZi0xOWU5ZjYxMjA3MmYifQ.V1IDoKZ25qke-lZlu8uBX95TWuyfTFfu1AGqu6X7TWI' }
    )
    return response1.json()
    # responseJson = response1.json()['result']
    # continuationToken = responseJson['continuationToken']