class Furniture():
    woodType = "Teakwood"

class Chair(Furniture):
    def __init__(self):
        self.__numberLegs = 4

    def checkLegs(self):
        print('you have {} legs left on this chair'.format(self.__numberLegs))

    def newWood(self, wood):
        self.woodType = wood
        print("your chair is now made of {} wood".format(self.woodType))
    def sawLegOff(self):
        if self.__numberLegs > 0:
            self.__numberLegs = self.__numberLegs -1
            print("you just sawed a leg off... only {} left".format(self.__numberLegs))
        else:
            print("there are no legs left to saw off!")

chair = Chair()

while True:
    print("1: Pick new wood")
    print("2: check legs")
    print("3: saw off leg")
    print("4: Exit")
    choice = int(input())
    if choice == 1:
        print("what do you want your new wood type to be?")
        chair.newWood(input().title())
    elif choice == 2:
        chair.checkLegs()
    elif choice == 3:
        chair.sawLegOff()
    elif choice == 4:
        exit()
    else:
        print("Please pick a value shown")

