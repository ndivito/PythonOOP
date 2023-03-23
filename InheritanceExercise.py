class Furniture():
    woodType = "Teakwood"

class Chair(Furniture):
    def __init__(self):
        self.__numberLegs = 4

    def checkLegs(self):
        print('you have {} legs left on this chair'.format(self.__numberLegs))

    def newWood(self):
        print("what do you want your new wood type to be?")
        self.woodType = input().title()
        print("your chair is now made of {} wood".format(self.woodType))
    def sawLegOff(self):
        if self.__numberLegs > 0:
            self.__numberLegs = self.__numberLegs -1
            print("you just sawed a leg off...")
        else:
            print("there are no legs left to saw off!")

chair = Chair()
chair.newWood()
chair.checkLegs()
chair.sawLegOff()
chair.checkLegs()
print("your chair woodtype is {}".format(chair.woodType))
print("your chair has this many legs : {}".format(chair._numberLegs))
chair._numberLegs = 2