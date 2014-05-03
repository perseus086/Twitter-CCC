#No hay nada solo un metodo que voy a llamar desde arguments 1

def imprimir_hola():
    print "hola desde ejemplo 1"

def imprimir_con_argumentos(num, word):
    print 'desde ejemplo1/imprimir con argumentso'
    for n in range(num):
        print word

def multiplica_por_2(num):
    return 2*num