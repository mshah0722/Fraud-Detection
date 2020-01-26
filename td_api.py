import requests
import json

API_KEY = 'API KEY'


def get_transations_by_customer(id):
    response = requests.get(
        'https://api.td-davinci.com/api/customers/' + id + '/transactions',
        headers={'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDQlAiLCJ0ZWFtX2lkIjoiODllZjBiNGYtMGU4Zi0zMmZkLThjYWEtNTFjOTdkYWFjYzgwIiwiZXhwIjo5MjIzMzcyMDM2ODU0Nzc1LCJhcHBfaWQiOiI3ZDFmNzUzNi02M2Q0LTRjZTgtYmVmZi0xOWU5ZjYxMjA3MmYifQ.V1IDoKZ25qke-lZlu8uBX95TWuyfTFfu1AGqu6X7TWI'}
    )
    json_data = json.loads(response.text)
    return json_data['result']


def get_all_customer_data():

    response = requests.post(
        'https://api.td-davinci.com/api/raw-customer-data',
        headers={'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDQlAiLCJ0ZWFtX2lkIjoiODllZjBiNGYtMGU4Zi0zMmZkLThjYWEtNTFjOTdkYWFjYzgwIiwiZXhwIjo5MjIzMzcyMDM2ODU0Nzc1LCJhcHBfaWQiOiI3ZDFmNzUzNi02M2Q0LTRjZTgtYmVmZi0xOWU5ZjYxMjA3MmYifQ.V1IDoKZ25qke-lZlu8uBX95TWuyfTFfu1AGqu6X7TWIs'}
    )

    json_data = json.loads(response.text)
    return json_data['result']['customers']
