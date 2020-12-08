import requests
from flight_data import FlightData


KIWI_API_QUERY = "_YOUR_TEQUILIA_API_"
KIWI_QUERY_END = "https://tequila-api.kiwi.com"



class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{KIWI_QUERY_END}/locations/query"
        headers = {"apikey": KIWI_API_QUERY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": KIWI_API_QUERY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }
        kiwi_response = requests.get(
            url=f"{KIWI_QUERY_END}/v2/search",
            headers=headers,
            params=query,
        )
        data = kiwi_response.json()["data"][0]

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_air=data["route"][0]["flyFrom"],
            dest_city=data["route"][0]["cityTo"],
            dest_air=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.dest_city}: ${flight_data.price}")
        return flight_data


