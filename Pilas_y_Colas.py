import sys
from collections import deque
class Pila:
    def __init__(self,size):
        self.size=size

    def push(self):
        cant=int(input("¿Cuántos valores va a ingresar a la pila?: "))
        elementos = 0
        for tamanio in range(cant):
            valor=input("Ingrese un valor: ")
            elementos += 1
            tamanio+=elementos
            tamanio=tamano.append(valor)
        submenuPilas()

    def pop(self):
        if len(tamano) > 0:
            while len(tamano):
                siguiente=tamano.pop()
                print("Elemento eliminado de la pila:",siguiente)
                print("Pila actual",tamano)
                print()
            submenuPilas()
        else:
            print("La Pila está vacía")
        submenuPilas()

    def size(self):
        if len(tamano) > 0:
            long=len(tamano)
            print("La longitud de la cola es: ", long)
            submenuPilas()
        else:
            print("La Pila está vacía")
        submenuPilas()

    def show(self):
        if len(tamano) > 0:
            print("La pila contiene: ", len(tamano) , " elementos." )
            print(tamano[::-1])
        else:
            print("La Pila está vacía")
        submenuPilas()

    def insertar(sel):
        cant=int(input("¿Cuántos valores va a ingresar a la pila?: "))
        elementos= 0
        for tamanio in range(cant):
            valor=input("Ingrese un valor: ")
            elementos += 1
            tamanio+=elementos
            tamanio=tamano.append(valor)
        print(tamano[::-1])
        submenuPilas()

    def buscar(self):
        x=input("Ingrese elemento a buscar: ")
        if x in tamano:
            print("Elemento",x, "se  encuentra en pila")
        else:
            print("Elemento ",x,"no se  encuentra en pila")
        submenuPilas()
        
tamanio=0
tamano=[]
#_____________________
def menu():
    print("-Escoja una de las siguientes opciones-")
    print("1.Pilas\n2.Colas") 
    seleccion=int(input("Ingrese seleccion: "))
    if seleccion == 1:
        print("-Escogió Pilas-")
        submenuPilas()
    elif seleccion == 2:
        print("-Escogió Colas-\n" )
        submenuColas()
    elif seleccion > 2 or seleccion < 1:
        print("Valor no válido, vuelva a ingresar.") 
        menu()

def submenuPilas():
    print("Escoja una subopción:")
    print("""
    *__________________________________________*
    |                                          |
    |            Menu De Opciones              |
    |__________________________________________|
    |      1. Push                             |
    |      2. Pop                              |
    |      3. Show                             |
    |      4. Longitud                         |
    |      5. Insertar                         |
    |      6. Buscar                           |
    |      7. Salir                            |
    |      8. Volver a Menu                    |
    *__________________________________________* """)
    print(""" """)
    
    subseleccion = int(input("Ingrese su selección:"))
    if subseleccion == 1:
        print("-Escogió Push-")
        print(""" """)
        Pila.push(0)
    elif subseleccion == 2:
        print("-Escogió Pop-")
        Pila.pop(0)
        
    elif subseleccion == 3:
        print("-Escogió Show-")
        Pila.show(0)

    elif subseleccion == 4:
        print("-Escogió Longuitud-")
        Pila.size(0)

    elif subseleccion == 5:
        print("-Escogió Insertar-")
        Pila.insertar(0)

    elif subseleccion == 6:
        print("-Escogió Buscar-")
        Pila.buscar(0)
    
    elif subseleccion == 7:
        print("-Gracias por usar el codigo ^-^")
        sys.exit(0)
        
    elif subseleccion == 8:
        menu()
    
    elif subseleccion > 8 or subseleccion < 1:
        print("Valor no válido, vuelva a ingresar.") 
        submenuPilas()

class Cola():
    def __init__(self,size):
        self.size=size
    
    def push(self):
        cant=int(input("¿Cuántos valores va a ingresar a la cola?: "))
        elementos = 0
        for tamanio in range(cant):
            valor=input("Ingrese un valor : ")
            elementos += 1
            tamanio+=elementos
            tamanio=tamanoo.append(valor)
        print(tamanoo)
        submenuColas()

    def pop(self):
        if len(tamanoo) > 0:
            while len(tamanoo):
                siguiente=tamano.popleft()
                print("Elemento eliminado:",siguiente,
                ".Elementos restantes:",tamano)
            submenuColas()
        else:
            print("La Cola está vacía")
            submenuColas()

    def size(self):
        long=len(tamanoo)
        print("La longitud de la cola es: ", long)
        submenuColas()

    def show(self):
        if len(tamanoo) > 0:
            print("LA COLA CONTIENE: ", len(tamanoo) , " ELEMENTOS." )
            print(tamanoo)
        else:
            print("La Cola está vacía")
        submenuColas()

    def insertar(self):
        cant=int(input("¿Cuántos valores va a ingresar a la cola?: "))
        elementos= 0
        for tamanio in range(cant):
            valor=input("Ingrese un valor: ")
            elementos += 1
            tamanio+=elementos
            tamanio=tamanoo.append(valor)
        print(tamanoo)
        submenuColas()

    def buscar(self):
        if len(tamanoo) > 0:
            x=input("Ingrese elemento a buscar: ")
            if x in tamanoo:
                print("Elemento encontrado")
            else:
                print("Elemento no encontrado")
            submenuColas()
        else:
            print("La Cola está vacía")
            submenuColas()
tamanio=0
tamanoo=[]
tamanoo=deque(tamanoo, maxlen=6)

def submenuColas():
    print("Escoja una subopción:")
    print("""
    *__________________________________________*
    |                                          |
    |            Menu De Opciones              |
    |__________________________________________|
    |      1. Push                             |
    |      2. Pop                              |
    |      3. Show                             |
    |      4. Longitud                         |
    |      5. Insertar                         |
    |      6. Buscar                           |
    |      7. Salir                            |
    |      8. Volver a Menu                    |
    *__________________________________________* """)
    print(""" """)
    
    subseleccion = int(input("Ingrese su selección:"))
    if subseleccion == 1:
        print("-Escogió Push-")
        print(""" """)
        Cola.push(0)
    elif subseleccion == 2:
        print("-Escogió Pop-")
        Cola.pop(0)
        
    elif subseleccion == 3:
        print("-Escogió Show-")
        Cola.show(0)

    elif subseleccion == 4:
        print("-Escogió Longuitud-")
        Cola.size(0)

    elif subseleccion == 5:
        print("-Escogió Insertar-")
        Cola.insertar(0)

    elif subseleccion == 6:
        print("-Escogió Buscar-")
        Cola.buscar(0)
    
    elif subseleccion == 7:
        print("-Gracias por usar el codigo ^-^")
        sys.exit(0)

    elif subseleccion == 8:
        menu()
        
    elif subseleccion > 8 or subseleccion < 1:
        print("Valor no válido, vuelva a ingresar.") 
        submenuColas()

menu()