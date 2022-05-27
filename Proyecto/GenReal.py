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

Created on Wed May 18 13:15:19 2022

@author: tania
"""

import numpy as np
import math
import random

class GenReal:
    def __init__(self, min, max, nbits = 16):
        self.max = max # max es el maximo valor que puede alcanzar un coeficiente
        self.nbits = nbits
        self.min = min  #min es el minimo valor que puede tener un coeficiente
        self.npart = int(math.pow(2, self.nbits)) # npart partes en que se divide el problema
        self.delta = (abs(min-max)/self.npart)#el valor de la particion

    def initGen(self):
        self.gen = random.choices([0,1], k = self.nbits) #genera
        while not self.isValid(): #si no esta entre los valores establecidos lo vuelve a generar
            self.gen = random.choices([0,1], k = self.nbits)

    def isValid(self):
        value = self.getValue() #convierte binario a decimal
        if value >= self.min and value <= self.max:  # evalua si el numero creado esta dentro de los parametros establecidos
            return True
        else:
            return False

    def cruzar(self, genMadre):
        padre = self.gen.copy() #padre es la copia de si mismo
        madre = genMadre.gen.copy()
        cps1 = int(np.floor((self.nbits-1)/3)) # punto de corte 1
        cps2 = 2*cps1 #punto de corte 2

        #se cruza de la manera padre-madre-padre
        h1 = padre[0:cps1]
        h1.extend(madre[cps1:cps2])
        h1.extend(padre[cps2:])

        #se cruza de la manera madre-padre-madre
        h2 = madre[0:cps1]
        h2.extend(padre[cps1:cps2])
        h2.extend(madre[cps2:])

        #se crean los hijos
        s1 = GenReal(self.min, self.max, self.nbits)
        s2 = GenReal(self.min, self.max, self.nbits)
        #a cada hijo se le especifica un gen (las cruzas hechas anteriormente)
        s1.gen = h1
        s2.gen = h2

        return[s1,s2] #regresa los dos hijos

    def mutar(self):
        self.initGen()

    def __str__(self):
        return str(self.gen)

    def getValue(self):
        numP = int(''.join([str(i) for i in self.gen[:]]),2)
        #Como nuestra solucion debe ser con números enteros se redondea el numero al mas cercano
        valor = round(self.min + self.delta * numP)
        return valor
