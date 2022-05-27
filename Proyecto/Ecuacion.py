# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
Unidad de aprendizaje: Algortimos Genéticos
Author:
    Bernal González Sergio David
    Carrillo Martínez Leonardo Javier
    Del Angel Hernández Tania Ameyalli

Descripción: Esta clase genera una ecuacion lineal aleatoria

Created on Wed May 18 12:35:05 2022

@author: tania
"""

import random
import numpy as np

class Ecuacion:
    def __init__(self, numPar, min, max):
        self.min = min
        self.max = max
        self.nP = numPar
        self.ec = ""
        self.coeficientes = []
        var = "abcdefghij"
        self.variables = list(var)


    def init(self):
        ec=""
        if self.nP<=10:

            #Por cada numero de parametros creamos un coeficiente
            for i in range(self.nP):
                coefAux = random.randint(self.min, self.max)
                #Guradamos los coeficientes generados
                self.coeficientes.append(coefAux)

                #Si el indice no es 0 y el coeficiente es mayor o igual a 0 se agrega un '+' a la cadena que representa nuestra ecuacion
                if i!=0 and coefAux>=0:
                    ec+="+"
                    ec+=str(coefAux)
                    #Se agrega una variable a la ecuacion
                    #P.ej:
                        # coefAux = 3
                        # variables[i] = b
                        # ex+=: +3b
                    ec+=self.variables[i]
                else:
                    ec+=str(coefAux)
                    ec+=self.variables[i]

            #Igualdad de la ecuacion
            ec+="="
            #Resultado para la ecuacion generada
            res = random.randint(-500, 500)
            ec+=str(res)
            self.ec = ec
            self.res = res
        #Restricion de que solo sean 10 numeros de parametros
        else:
            print("Excede el numero de parametros!")
            return

    def generarMaxYMin(self):
        #Se generan los maximos y minimos para la ecuacion, en este caso
        #los minimos representan el valor negativo del resultado y los maximos el valor positivo
        self.maximos = []
        self.minimos =[]
        self.nbits = []

        for i in range(self.nP):
            if self.res > 0:
                self.maximos.append(self.res)
                self.minimos.append((-1)*self.res)

            else:
                self.minimos.append(self.res)
                self.maximos.append((-1)*self.res)
            self.nbits.append(16)
