from Cromosome import *

if __name__ == "__main__":
    clave = Cromosome()

    print(clave.toString())
    b = 1 if clave.getBitAtGen(1) == 0 else 0
    clave.setBitAtGen(1, b)
    print(f"Cromosoma Gen1 = {clave.getBitAtGen(1)}")
    print(clave.toString())
