class Flight:
    airline_name = ''
    flight_number = ''
    flight_status = ''

    def __init__(self, flight_number, airline_name, flight_status):
        Flight.flight_number = flight_number
        Flight.airline_name = airline_name
        Flight.flight_status = flight_status

    def get_airline(self):
        return self.flight_number, self.airline_name, self.flight_status


class Person:
    first_name = ''
    last_name = ''

    def __init__(self, first_name, last_name):
        Person.first_name = first_name
        Person.last_name = last_name

    def get_information(self):
        return self.first_name, self.last_name


class Employee(Person):

    def __init__(self, first_name, last_name, employeeID):
        Person.__init__(self, first_name, last_name)
        self.employeeID = employeeID

    def get_employee(self):
        return Person.first_name, Person.last_name, self.employeeID


class Passenger(Person):

    def __init__(self, first_name, last_name, gateNo, __DoB):  # __DoB here resembles member of private details of data
        Person.__init__(self, first_name, last_name)
        self.gateNo = gateNo
        self.__DoB = __DoB

    def get_passenger(self):
        return Person.first_name, Person.last_name, self.gateNo, self.__DoB


# performed multiple inheritance as mentioned
class BaggageCount(Flight, Person):

    def __init__(self, first_name, last_name, flight_number, airline_name, flight_status, bags_count):
        Person.__init__(self, first_name, last_name)
        Flight.__init__(self, flight_number, airline_name, flight_status)
        self.bags_count = bags_count

    def get_baggages(self):
        return (Person.first_name, Person.last_name, Flight.flight_number, Flight.airline_name,
                Flight.flight_status, self.bags_count)


l = Flight(Flight.flight_number, Flight.airline_name, Flight.flight_status)
m = Person(Person.first_name, Person.last_name)
n = Employee(Person.first_name, Person.last_name, "703246")
o = Passenger(Person.first_name, Person.last_name, "C12", "01/01/1993")
q = BaggageCount("Huzaifa", "Hussain", "CX4674", "Cathay pacific", "On time", 2)

print(m.get_information())
print(n.get_employee())
print(q.get_baggages())
