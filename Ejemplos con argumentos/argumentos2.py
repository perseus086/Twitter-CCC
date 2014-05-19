

'''
Una opcion para argumentos desde el systema
Funciona Parecido que en java el String args[]

1. llamar a import sys
2. sys.argv[n] tiene el argumento que se quiere
3. sys.argv[0] es el nombre del programa
4. sys.argv[1] es el primer argumento
5. sys.argv[2] es el segundo. Y asi
6. Como el primer agumneto (el numero 0) es el nombre del programa
    entonces si se quieren 2 argumentos el len(sys.argv) debe ser 3
    porque hay que sumarle 1 del argumento 0

aqui pongo ejemplo con 2 argumentos
'''

import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.stderr.write('Error: se necesitan mas argumentos\n <nombre><numero>')
        sys.exit()
    else:

        nombre = sys.argv[1]
        num = int(sys.argv[2])   #Se deberia hacer un try a ver si vale hacer este casting sino botar error

        print nombre, num*2


