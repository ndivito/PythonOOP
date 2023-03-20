class CarRental:
    def __init__(self, cars):
        self.cars = cars

    def calculateFare(self,car):
        print('How many days do you want the car?')
        days = int(input())
        print()
        print('You must pay ', days*int(self.cars[car]))

    def rentCar(self):
        print('What kind of car do you want to rent?')
        for car in self.cars:
            print(car)
        selection = input()
        if selection in self.cars:
            self.calculateFare(selection)
        else:
            print('sorry, no such car')



cars = {
    'Hatchback': 30,
    'Sedan': 50,
    'SUV': 100
}

avis = CarRental(cars)
avis.rentCar()