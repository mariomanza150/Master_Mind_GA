import random

class Gene:
    __bit = 0

    def __init__(self):
        self.bit = random.randint(0,1)

    def getBit(self):
        return self.bit
    
    def setBit(self, b):
        self.bit = b
    
    def isZero(self):
        return True if self.bit == 0 else False

    def isOne(self):
        return True if self.bit == 1 else False

    def toString(self):
        return str(self.bit)