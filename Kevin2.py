# Make a program that runs continuously
# Program will consist of Bicycles
# Program will allow you to choose how many wheels you have on your bicycle and the brand to choose from

class Bicycles():
    TerrainType = "Road"  # The most popular type of terrain to ride your bike one


class MountainBike(Bicycles):  # Subclass type of Bicycles
    def __init__(self):  # Allowing the function to be ran
        self.__numberOfWheels = 2  # number of wheels a bicycle has
        self.__numberOfPedals = 2  # number of pedals a bicycle has
        self.__mostPopularBrand = "Specialized"
        self.__secondMostPopularBrand = "Trek"

    def checkWheels(self):
        print("Your mountain bike has {} wheels ".format(self.__numberOfWheels))

    def checkPedals(self):
        print("Your mountain bike has {} pedals ".format(self.__numberOfPedals))

    def BikeType(self, brand):
        self.brandtype = brand
        print(
            "{} is your favotire type of mountain bike, while {} is the most popular bike brand out there followed by {}".format(
                self.brandtype, self.__mostPopularBrand, self.__secondMostPopularBrand))

    def WheelChoice(self):
        print("Would you like to add or subtract Wheels")
        userinput = input()  # String
        numWheels = 0
        if userinput == "add":
            print("How many would you like to add?")
            numWheels = int(input())
        elif userinput == "subtract":
            while True:
                print("How many would you like to remove?")
                numWheels = int(input()) * -1
                if self.__numberOfWheels + numWheels >= 0:
                    break
                else:
                    print("You cannot have a negative number of wheels, please choose another number!")
        self.__numberOfWheels = self.__numberOfWheels + numWheels
        print("Your bike has {} wheels".format(self.__numberOfWheels))

    def PedalChoice(self):
        print("Would you like to add or subtract Pedals")
        userinput = input()  # String
        numPedals = 0
        if userinput == "add":
            print("How many would you like to add?")
            numPedals = int(input())
        elif userinput == "subtract":
            while True:
                print("How many would you like to remove?")
                numPedals = int(input()) * -1
                if self.__numberOfPedals + numPedals >= 0:
                    break
                else:
                    print("You cannot have a negative number of pedals, please choose another number!")
        self.__numberOfPedals = self.__numberOfPedals + numPedals
        print("Your bike has {} pedals".format(self.__numberOfPedals))


bike = MountainBike()

while True:
    print("1: Pick your favorite Mountain Bike Brand")
    print("2: Check how many wheels/pedals your bike has")
    print("3: Add or get rid of a wheel")
    print("4: Add or get rid of a pedal")
    print("5: Exit")
    choice = int(input())
    if choice == 1:
        print("What is your favorite Mountain Bike brand out there?")
        bike.BikeType(input())
    elif choice == 2:
        bike.checkWheels()
        bike.checkPedals()
    elif choice == 3:
        bike.WheelChoice()
    elif choice == 4:
        bike.PedalChoice()
    elif choice == 5:
        exit()
    else:
        print("Pick a value shown above of 1 through 5 so this program runs properly!")





