#   ALGORITMO GENETICO SIMPLE
#AUTOR: Vander Catti Idme
#FECHA: 13/10/2019
#Para el curso de Inteligencia Computacional
############################################

import random
import math

class individuo(object):

    #CONSTRUCTOR DE LA CLASE INDIVIDUO 
    def __init__(self, puntaje = 0):
        #ATRIBUTOS
        self.gen = random.randrange(101)
        self.puntaje = puntaje

    #METODOS   

    def decimalBinario(self):
        genArray=[0,0,0,0,0,0,0,0]
        temporal = self.gen
        i = 7

        while temporal >= 1:  
            
            residuo = temporal % 2
            genArray[i]=residuo
            temporal /= 2
            temporal = int(temporal)
            i -= 1

        return genArray

    #asigna el puntaje
    def conocerPuntaje(self):
        self.puntaje = math.sqrt(self.gen)
        return self.puntaje


#------------------------------------------------------------------------
#------------------------------------------------------------------------


def imprimirPoblacion(indP):
    
    for i in range(0,6):
        print("Invividuo %d: %d %s %d" % (i, indP[i].gen, indP[i].decimalBinario(), indP[i].conocerPuntaje() ))
       

# SELECCION: Se forman parejas de dos individuos extremos con extremos, luego se compara
# su puntaje que es obtenido mediante f(x) = x sqrt 2, x es el individuo en si, en este caso 
# un numero aleatorio del 0 al 10, de las parejas formadas se escoge el que tiene menor 
# puntaje y se le asigna a la a una nueva poblacion, para completar nuestra nueva pobla-
# cion se generan nuevos individuos con valores aleatorios.

def seleccion(indS):

    i = 0
    j = 5 

    temporalS = [individuo(),individuo(),individuo(),individuo(),individuo(),individuo()]

    for i in range(0,3):
        if indS[i].conocerPuntaje() < indS[j].conocerPuntaje():
            temporalS[i] = indS[i]
            print("Escogido: %d" % indS[i].gen)
        else:
            temporalS[i] = indS[j]
            print("Escogido: %d" % indS[j].gen) 
        j -= 1   
    print("***********")
    return temporalS


def cruce(indC):
    
    randomgen = random.randrange(1,8)                # coger aleatoriamente un gen a partir del 1
    padre = [0,0,0,0,0,0,0,0]
    madre = [0,0,0,0,0,0,0,0]
    tmp = 0
  
    # Escoger pareja aleatorio
    randompareja1 = random.randrange(0,6)            # Escogemos un individuo al asar
    randompareja2 = aleatorioNoRep(randompareja1)    # Escogemos otro individuo al azar distinto del primero

    padre = indC[randompareja1].decimalBinario()
    madre = indC[randompareja2].decimalBinario()
         
    print("Pareja: ")
    print("--------")
    print("padre: %d %s (%d)" % (indC[randompareja1].gen, indC[randompareja1].decimalBinario(), randompareja1 ))
    print("madre: %d %s (%d)" % (indC[randompareja2].gen, indC[randompareja2].decimalBinario(), randompareja2 ))
    print("  ")

    for i in range(randomgen):
          tmp = padre[i]
          padre[i] = madre[i]
          madre[i] = tmp

    if indC[randompareja1].gen > binarioDecimal(padre):
        indC[randompareja1].gen = binarioDecimal(padre)
    else:
        print("no descendencia padre!") 

    if indC[randompareja2].gen > binarioDecimal(madre):
        indC[randompareja2].gen = binarioDecimal(madre)
    else:
        print("no descendencia madre!") 
    

    print("Hijos: ")
    print("-------")
    print("%d %s %d" % (indC[randompareja1].gen, indC[randompareja1].decimalBinario(), randomgen))
    print("%d %s %d" % (indC[randompareja2].gen, indC[randompareja2].decimalBinario(), randomgen))
    print("***********")
    
    return indC
    
def mutacion(indM):
    randomMutante = random.randrange(0,6)
    randomGen = random.randrange(0,8)

    mutante = [0,0,0,0,0,0,0,0]

    mutante = indM[randomMutante].decimalBinario()

    print("Escogido -> individuo: %d = %d %s"% (randomMutante,indM[randomMutante].gen, indM[randomMutante].decimalBinario() ))
    print("Gen a mutar %d"% randomGen)
    


    if mutante[randomGen] == 0 :
        mutante[randomGen] = 1
    else:
        mutante[randomGen] = 0


    if indM[randomMutante].gen > binarioDecimal(mutante):

        indM[randomMutante].gen = binarioDecimal(mutante)
        print("MUTANTE:    %d %s" % (indM[randomMutante].gen, indM[randomMutante].decimalBinario() ))
        print("***********")
    
    else:
        print("no se muto!") 

    
    


    return indM       

# Funcion aleatorioNoRep garantiza que la pareja formada sea de dos individuos distintos   
def aleatorioNoRep(a):
    b = random.randrange(0,6)
    while a == b :
        b = random.randrange(0,6)

    return b


# Para poder asignar correctamente los hijos de las parejas formadas es necesario convertir 
# la cadena de 1 y 0 a decimal, para posteriormente guardar la cadena del nuevo numero

def binarioDecimal(cadena):
    suma = 0
    j = 7
    for i in range(0,8):
        suma +=  (cadena[i]*(2**j))
        j -= 1
    return suma


def mejorDeLaPoblacion(indP, iteracion):
    mejor = 0
    mejora = 0
    mejor = indP[0].conocerPuntaje()
    for i in range(len(indP)):
        if mejor > indP[i].conocerPuntaje():
            mejor = indP[i].conocerPuntaje()
            mejora = indP[i].gen
    
    print("%d de la iteracion %d" % (mejora,iteracion))




if __name__ == "__main__":
    
    
    #poblacion inicial
    i = 0
    print("-------------------Poblacion Inicial--------------------------------")
    print("--------------------------------------------------------------------")
    poblacion = [individuo(),individuo(),individuo(),individuo(),individuo(),individuo()]
    imprimirPoblacion(poblacion)

    print("----------------------Seleccion-------------------------------------")
    print("--------------------------------------------------------------------")
    poblacionSeleccion = seleccion(poblacion)
    imprimirPoblacion(poblacionSeleccion)

    print("------------------------Cruce---------------------------------------")
    print("--------------------------------------------------------------------")
    poblacionCruce = cruce(poblacionSeleccion)
    imprimirPoblacion(poblacionCruce)

    print("-----------------------Mutacion-------------------------------------")
    print("--------------------------------------------------------------------")
    poblacionMutacion = mutacion(poblacionCruce)
    imprimirPoblacion(poblacionMutacion)

    print("MEJOR**************")
    mejorDeLaPoblacion(poblacionMutacion,i)
    print("*******************")
    
    
    for i in range(1,30):
        print("----------------------Seleccion-------------------------------------")
        print("--------------------------------------------------------------------")
        poblacionSeleccion = seleccion(poblacionMutacion)
        imprimirPoblacion(poblacionSeleccion)

        print("------------------------Cruce---------------------------------------")
        print("--------------------------------------------------------------------")
        poblacionCruce = cruce(poblacionSeleccion)
        imprimirPoblacion(poblacionCruce)

        print("-----------------------Mutacion-------------------------------------")
        print("--------------------------------------------------------------------")
        poblacionMutacion = mutacion(poblacionCruce)
        imprimirPoblacion(poblacionMutacion)

        print("MEJOR**************")
        mejorDeLaPoblacion(poblacionMutacion,i)
        print("*******************")
    