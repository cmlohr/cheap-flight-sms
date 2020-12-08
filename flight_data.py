class FlightData:
    def __init__(self, price, origin_city, origin_air, dest_city, dest_air, out_date, return_date,
                 via_city="", stop_over=0):
        self.price = price
        self.origin_city = origin_city
        self.origin_air = origin_air
        self.dest_city = dest_city
        self.dest_air = dest_air
        self.out_date = out_date
        self.return_date = return_date
        self.via_city = via_city
        self.stop_over = stop_over
