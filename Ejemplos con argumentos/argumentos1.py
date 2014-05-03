####Ejemplo para usar metodos en otro archivo con y sin argumentos.



import ejemplo1

def main():
    ejemplo1.imprimir_hola()
    ejemplo1.imprimir_con_argumentos(2, 'Ejemplo')
    n = ejemplo1.multiplica_por_2(4)
    print 'n=', n

#1.
###################
#Equivalente a main en Java. No es obligatorio. Pero es bueno usar
#el programa entra directamente al codigo que tenga este if. En este
## caso va a ejecutar la funcion main que esta arriba.
#Lastimosamente los metodos tienen que estar arriba de lo que se
# quiere ejecutar o en otro archivo. Como se pone arriba t odo llega un punto
##en que es demaciado grande

#les recomiendo que hagan un monton de archivos con metodos pequenas.

#en un archivo dentro de la misma carpeta voy a llamar a un metodo aparte
#para eso debes poner import y el nombre del otro archivo y ahi si el nombre del metodo

if __name__ == "__main__":
    main()