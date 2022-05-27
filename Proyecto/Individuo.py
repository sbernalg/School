# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
Unidad de aprendizaje: Algortimos Genéticos
Author: Del Angel Hernández Tania Ameyalli
Descripción:

Created on Wed May 18 18:10:03 2022

@author: tania
"""

import random
import numpy as np
from CromosomaReal import CromosomaReal as CR
class Individuo:
    def __init__(self, minis, maxis, nbits):
        self.minis = minis
        self.maxis = maxis
        self.nbits = nbits
        self.cromosoma = CR(self.minis, self.maxis, self. nbits)

    def init(self):
        self.cromosoma.init()
        #Genera un cromosoma aleatorio, con los minis y maxis que nos dieron , este caso el tamaño del cromosoma es el numero de bits

    def cruza(self, mother):
        #creamos un cromosoma papa
        papa = CR(self.minis, self.maxis, self.nbits)
        papa.init()

        #creamos un cromosoma mama
        mama = CR(self.minis, self.maxis, self.nbits)
        mama.init()

        #los cruzamos
        hijos = papa.cruzar(mama)

        #Creamos nuevos individuos (hijos) y les indicamos su cromosoma
        ind1 = Individuo(self.minis, self.maxis, self.nbits)
        ind1.cromosoma = hijos[0]
        ind2 = Individuo(self.minis, self.maxis, self.nbits)
        ind2.cromosoma = hijos[1]

        #Regresamos a los hijos(cruzas)
        return [ind1, ind2]

    def __str__(self):
        #sobre escribe el metodo str, regresa el cromosoma
        return self.cromosoma.__str__()
    def mutar(self):
        #Se manda a llamar a mutar el cromosoma
        self.cromosoma.mutar()
