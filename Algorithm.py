from Gene import *

class Algorithm:
    def __init__(self):
        gen1 = Gene()
        
        print(f"gen1 = {gen1.toString()}")
        msg = "cero" if gen1.isZero() else "uno"
        print(f"Bit de gen1 es {msg}")

        gen2 = Gene()
        gen2.setBit(gen1.getBit())
        print(f"gen2 = {gen1.toString()}")

if __name__ == "__main__":
    Algorithm()