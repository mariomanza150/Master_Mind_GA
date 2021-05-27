import random

class Gene:
    bit = 0

    def __init__(self):
        self.bit = random.randint(0,1)

    def getBit(self):
        return self.bit
    
    def setBit(self, b):
        self.bit = b

    def toString(self):
        return str(self.bit)
