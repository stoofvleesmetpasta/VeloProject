import random

pers = []

class Person():
    def __init__(self):
        self.movement = False
        self.bike = None
        self.name = Person.NameGen()

    def NameGen():
        firstnames = ["Alex", "Sandra", "Raf", "Kim", "John", "Enya", "Joseph", "Jotaro", "Jonathan", "Kakyoin", "Dio", "Polnareff", "Mohammed", "Lisa", "Asthel"]
        lastnames = ["Joestar", "Jean-Pierre", "Noriaki", "Brando", "Avdol", "Jefferson", "Cujoh", "Lisa", "Vanreusel", "De Bie", "Lauwers", "Vercouteren"]
        definedname = random.choice(firstnames) + " " + random.choice(lastnames)
        return definedname

class Bike():
    def __init__(self):
        self.bikeId = None
        self.slot = None

class Station():
    def __init__(self):
        self.stationId = None
        self.bikes = []

class slot():
    def __init__(self):
        self.isOccupied = False
        