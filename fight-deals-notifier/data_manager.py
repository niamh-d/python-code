from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = ""
SHEETY_AUTHORIZATION = ""


class DataManager:

    def __init__(self):
        self.destination_data = {}

        self.headers = {
            "Authorization": SHEETY_AUTHORIZATION
        }

    def get_destination_data(self):
        # response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.headers)
        # data = response.json()
        # print(data)
        # self.destination_data = data["prices"]
        # return self.destination_data

        self.destination_data = [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2},
                {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 3},
                {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4},
                {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5},
                {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6},
                {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7},
                {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8},
                {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9},
                {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 10},
                {'city': 'Bali', 'iataCode': 'DPS', 'lowestPrice': 501, 'id': 11}]

        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.headers,
            )
            print(response.text)
