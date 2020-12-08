import requests

SHEET_END = "_YOUR_SHEETY_END_POINT_"

# get sheety


class DataManager:

    def __init__(self):
        self.sheet_data = {}

    def get_data(self):
        response = requests.get(url=SHEET_END)
        data = response.json()
        self.sheet_data = data["sheet1"]

        return self.sheet_data

    def update_codes(self):
        for city in self.sheet_data:
            new_code = {
                "sheet1": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEET_END}/{city['id']}",
                json=new_code,
            )
            print(response.text)
