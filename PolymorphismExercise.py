class Square:
    def __init__(self,side):
        self.side=side

    def __pow__(self, power, modulo=None):
        return self.side ** power.side


square1 =Square(3)
square2 = Square(2)
print(square1 ** square2)
print(square2 ** square1)