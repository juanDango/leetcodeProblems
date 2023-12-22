from arrayProblems.arrays import print_menu_arrays
from twoPointers.twoPointers import print_menu_two_pointers
def runCode():

    print("Correr códigos de pruebas de leetcode exitosas, seleccione una opción: ")
    print("1. Array String")
    print("2. Two Pointers")

    entrada = input("Seleccione su opción: ")
    if entrada == "1":
        print_menu_arrays()
    if entrada == "2":
        print_menu_two_pointers()

    


if __name__ == "__main__":
    runCode()