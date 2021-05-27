from Gene import *

class Cromosome:
    genes = []

    def __init__(self):
        for _ in range(40):
            self.genes.append(Gene())
    
    def getBitAtGen(self, pos):
        return self.genes[pos].getBit()
    
    def setBitAtGen(self, pos, val):
        self.genes[pos].setBit(val)
    
    def showBinary(self):
        return ''.join([x.toString() for x in self.genes])

    def toString(self):
        return hex(int(self.showBinary(), 2))[2:]
