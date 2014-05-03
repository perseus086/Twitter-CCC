'''
Les recomiendo que usen la libreria argparse.

Voy a hacer un ejemplo con opciones que les pueden ser utiles
Este programa de una crea la ayuda. Queda bien pro.
Para ver la ayuda argumentos3.py -h o -help

Existen 2 tipos de argumentos: los opbligatorios y los que no.
Al inicio es mejor poner los obligatorios. Estos no van con
nada de palabras al inicio solo es el orden lo que importa

Los no obligatorios van con -a o --argumento




'''

import argparse

if __name__ == "__main__":

    #Datos del programa que aparecen en la ayuda

    parser = argparse.ArgumentParser(prog = "SUPER PROGRAMA",
                                     description="Este programa ",
                                     usage="python query.py [obligado] [name], for other arguments see -help")

    #argumento obligado
    parser.add_argument("obligado",
                        help = "Argumento obligado")


    #con choices vale hacer una lista de opciones que si no pones una de esas opciones te bota error y la ayuda y el programa cierra
    parser.add_argument("name",
                        choices=['abdera', 'aries', 'beehive'],
                        help = "Name of the forum to keep in the database (example: abdera, aries, behive...)")

    #Con default pueden poner paths o datos que van por default si no mandan nada en ese argumento y si mandan el argumento va lo que esta en el argumento
    parser.add_argument("-d",
                        "--database",
                        default  = "../data/db/inv_ind.db",
                        help = "Path of the inverted index database (default = ../data/db/inv_ind.db)")

    #Para integers te hace el casting de una
    parser.add_argument("-n",
                        "--num",
                        type=int,
                        default = 10,
                        help = "Depth of results to display (default = 10)")

    #te hace el casting a float de una
    parser.add_argument("--alpha",
                        type=float,
                        default = 1,
                        help = "alpha value (default = 1)")

    #para booleans se debe poner action store_true para ponerle en true cuando llaman al argumento y store_false pa dejarle en false
    parser.add_argument("-c",
                        "--c",
                        action = "store_true",
                        help = "Disables color print")

    ###IMPORTANTEEEEE: esta linea pone todos los argumentos anteriores en args
    args = parser.parse_args()

    obligado = args.obligado
    name = args.name
    database = args.database  #IMPORTANTE siempre este nombre corresponde al nombre que va con 2 guiones -- no con 1 guion
    numero = args.num   #No sirve con args.n siempre debe ir con el nombre del -- no -
    alpha = args.alpha
    color = args.c  # por default False


    print obligado, name, database, numero, alpha, color
