import requests
import json

API_KEY = 'API KEY'


def get_transations_by_customer(id):
    response = requests.get(
        "https://api.td-davinci.com/api/customers/52f7af91-e89b-495b-9beb-d7b267b7344e/transactions",
        headers={'Authorization': API_KEY}
    )
    json_data = json.loads(response.text)
    return json_data["result"]


def get_all_customer_data():

    response = requests.post(
        'https://api.td-davinci.com/api/raw-customer-data',
        headers={'Authorization': API_KEY}
    )

    json_data = json.loads(response.text)
    return json_data['result']['customers']
