import requests
import json

API_KEY = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDQlAiLCJ0ZWFtX2lkIjoiYTk1YTcwM2QtYzMzZS0zMjQzLThlMzAtMjk3YTcwZjEwNzU1IiwiZXhwIjo5MjIzMzcyMDM2ODU0Nzc1LCJhcHBfaWQiOiIyODA0ZmJjOS0wMjViLTRmZTgtODg2Mi1lNTM2ZDZhYWYyOWIifQ.mY0gqgaxkAaQRbvU-Id_WBHO9v6PnYVXmXaxmAnrJL0'


def get_transations_by_customer(id):
    response = requests.get(
        'https://api.td-davinci.com/api/customers/' + id + '/transactions',
        headers={'Authorization': API_KEY}
    )
    json_data = json.loads(response.text)
    return json_data['result']


def get_all_customer_data():

    response = requests.post(
        'https://api.td-davinci.com/api/raw-customer-data',
        headers={'Authorization': API_KEY}
    )

    json_data = json.loads(response.text)
    return json_data['result']['customers']
