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

    if flight is None:
        continue

    if flight.price < dest["lowestPrice"]:
        notify.send_message(
            message=f"PRICE ALERT! ${flight.price} to {flight.dest_city}-{flight.dest_air}, from {flight.out_date}."
        )

    if flight.price < dest["lowestPrice"]:
        user_list = data_manager.get_user()
        user_emails = [row["email"] for row in user_data]
        name = [row["firstName"] for row in user_data]
        message = f"PRICE ALERT! ${flight.price} to {flight.dest_city}-{flight.dest_air}, from {flight.out_date}."


        if flight.stop_over > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            print(message)

        google_link = f"https://www.google.com/flights?hl=en#flt={flight.origin_air}.{flight.dest_air}.{flight.out_date}*{flight.dest_air}.{flight.origin_air}.{flight.return_date}"
        # notify.send_message(message) commenting out turns off sms
        notify.send_email(user_emails, message, google_link)

