import json

import requests

BASE_URL = 'https://payme.uz/api/'


class PayMeApi:
    def __init__(self):
        pass

    def _make_request(self, params):
        response = requests.post(BASE_URL, data=json.dumps(params), verify=False)
        response_json = response.json()
        print(response_json)

        return response

    def users_check_phone(self, phone_number):
        params = {
            'jsonrpc': '2.0',
            'method': 'users.check_phone',
            'id': '1',
            'params': {
                'phone': phone_number
            }
        }
        response = self._make_request(params)

        return response

    def users_create(self, phone_number, password):
        params = {
            "jsonrpc": "2.0",
            "method": "users.create",
            "id": "1",
            "params": {
                "phone": phone_number,
                "location": {
                    "lat": 41.3240908,
                    "lon": 69.2240088
                },
                "password": password
            }
        }

        response = self._make_request(params)
        return response


a = PayMeApi()
a.users_check_phone('')
