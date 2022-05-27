# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
Unidad de aprendizaje: Algortimos Genéticos
Author:
    Bernal González Sergio David
    Carrillo Martínez Leonardo Javier
    Del Angel Hernández Tania Ameyalli

Descripción:

Created on Wed May 18 12:13:28 2022

@author: tania
"""

#Importamos las clases anteriores
from Individuo import Individuo
from Poblacion import Poblacion
from CromosomaReal import CromosomaReal as Real
from FitnessFunction import FitnessFunction as FF
import numpy as np
from AlgoritmoEvolutivo import AlgoritmoEvolutivo
from Ecuacion import Ecuacion as ec

#le pedimos al usuario que ingrese el numero de parametros
nuP = int(input("Ingrese el numero de parametros: "))

#hacemos uso de la clase Ecuacion para:
    #1. Crear la ecuacion
me = ec(nuP, -10, 10)
me.init()
    #2.Generar los minimos, maximos
me.generarMaxYMin()
# print("La ecuacion lineal es:\n")
# print(me.ec)
minimos = me.minimos
maximos = me.maximos
print(minimos)
print(maximos)
    #3. Obtener los coeficientes
coefic = me.coeficientes
    #4. Obtener la lista de bits a usar
nbits = me.nbits

#Imprimimos la ecuacion lineal generada
print("La ecuacion lineal generada es:\n")
print(me.ec)

#Hacemos uso de la clase Algortimo Evolutivo
ae = AlgoritmoEvolutivo(400, me.res, minimos, maximos, nbits, coefic)
#inicializamos
ae.inicializa()
#Imprimimos la primera generación
print("Primer generacion")
ae.showPob(True)
#Hacemos evolucionar la generación
for i in range(400):
    #print("GENERACION ",i)
    ae.evolucion()
#Imprimimos la ultima generación
print("----------------")
print("Ultima generacion")
ae.showPob(True)

mejor = ae.showElite();
valReal = mejor.cromosoma.getValues()


print("\n")
print("La ecuacion lineal generada es")
print(me.ec)
print("\n")
print("La mejor solucion fue")
print(valReal)

print("\n")
print("==================")
cad = ""
for i in range(nuP):
    coefAux = coefic[i]
    if i!=0 and coefAux>=0:
        cad+="+"
        cad+=str(coefAux)
        cad+="("+str(valReal[i])+")"
    else:
        cad+=str(coefAux)
        cad+="("+str(valReal[i])+")"

cad+="="
prod = np.dot(valReal, coefic)
cad+=str(prod)
print(cad)
print("==================")
