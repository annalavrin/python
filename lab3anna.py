class Airline:
    def __init__(self, destination, flight_number, aircraft_type, departure_time, weekdays):
        self.destination = destination
        self.flight_number = flight_number
        self.aircraft_type = aircraft_type
        self.departure_time = departure_time
        self.weekdays = weekdays

    def write_fields(self, destination, flight_number, aircraft_type, departure_time, weekdays):
        self.destination = destination
        self.flight_number = flight_number
        self.aircraft_type = aircraft_type
        self.departure_time = departure_time
        self.weekdays = weekdays

    def read_fields(self):
        return self.destination, self.flight_number, self.aircraft_type, self.departure_time, self.weekdays

# Создание списка объектов
flights = []
flights.append(Airline("London", "BA123", "Boeing 747", "10:00", ["Monday", "Wednesday", "Friday"]))
flights.append(Airline("Paris", "AF456", "Airbus A320", "14:30", ["Tuesday", "Thursday"]))
flights.append(Airline("New York", "DL789", "Boeing 787", "18:45", ["Saturday", "Sunday"]))
flights.append(Airline("London", "BA456", "Airbus A380", "13:15", ["Monday", "Wednesday", "Friday"]))
flights.append(Airline("Paris", "AF789", "Boeing 737", "16:50", ["Tuesday", "Thursday"]))

# Вывод списка рейсов для заданного пункта назначения
def get_flights_by_destination(flights, destination):
    flight_list = []
    for flight in flights:
        if flight.destination == destination:
            flight_list.append(flight)
    return flight_list

target_destination = "London"
destination_flights = get_flights_by_destination(flights, target_destination)
print("List of flights for destination:", target_destination)
for flight in destination_flights:
    print(flight.flight_number)

# Вывод списка рейсов для заданного дня недели:
def get_flights_by_weekday(flights, weekday):
    flight_list = []
    for flight in flights:
        if weekday in flight.weekdays:
            flight_list.append(flight)
    return flight_list

target_weekday = "Tuesday"
weekday_flights = get_flights_by_weekday(flights, target_weekday)
print("List of flights for weekday:", target_weekday)
for flight in weekday_flights:
    print(flight.flight_number)