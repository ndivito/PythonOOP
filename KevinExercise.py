# Make our own program that runs infanintly but you can exit
# Making a program that is about golf - stating that the driver is the most popular type of clubs
# Making a running program that allows you to pick how many irons/wedges you want in your bag

class Golf():
    clubType = "Driver" # Most people's favorite club is the Driver

class Iron(Golf): # Diverivative class of Golf
    def __init__(self): #allowing the function to be ran
        self.__numberOfIrons = 6 # Typical number of irons in a bag
        self.__numberofWedges = 4 # Typical number of wedges in a bag

    def checkIrons(self):
        print("You have {} irons in your set of clubs".format(self.__numberOfIrons))

    def checkWedges(self):
        print("You have {} wedges in your set of clubs".format(self.__numberofWedges))

    def newWood(self, wood):
        self.clubType = wood
        print("Your bag now has {} woods".format(self.clubType))

    def getRidOfIron(self):
        if self.__numberOfIrons > 0:
            self.__numberOfIrons = self.__numberOfIrons -1
            print("You just got rid of one of your irons, you have {} irons left in your bag!".format(self.__numberOfIrons))
        else:
            print("You decided to get rid of all your irons... Goodluck with that!")

    def getRidOfWedge(self):
        if self.__numberofWedges > 0:
            self.__numberofWedges = self.__numberofWedges -1
            print("You just got rid of one of your wedges, you now have {} wedges left in your bag!".format(self.__numberofWedges))
        else:
            print("You decided to get rid of all your wedges... Not a wise move!")


iron = Iron()


while True:
    print("1: Pick how many woods your bag has")
    print("2: Check number of wedges and irons")
    print("3: Get rid of an iron")
    print("4: Get rid of a wedge")
    print("5: Exit")
    choice = int(input())
    if choice == 1:
        print("How many woods would you like to have in your bag?")
        iron.newWood(input())
    elif choice == 2:
        iron.checkIrons()
        iron.checkWedges()
    elif choice == 3:
        iron.getRidOfIron()
    elif choice == 4:
        iron.getRidOfWedge()
    elif choice == 5:
        exit()
    else:
        print("Please pick a value shown above of 1 through 5")