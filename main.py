from datetime import datetime, timedelta
from flight_search import FlightSearch
from data_manager import DataManager
from sms_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_data()
flight_search = FlightSearch()
notify = NotificationManager()

ORIGIN_CITY = "_YOUR_ORIGIN_CITY_IATACODE_"

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(sheet_data)

    data_manager.destination_data = sheet_data
    data_manager.update_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_months = datetime.now() + timedelta(days=(6 * 30))

for dest in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY,
        dest["iataCode"],
        from_time=tomorrow,
        to_time = six_months
    )

    if flight.price < dest["lowestPrice"]:
        notify.send_message(
            message=f"PRICE ALERT! ${flight.price} to {flight.dest_city}-{flight.dest_air}, from {flight.out_date}."
        )


