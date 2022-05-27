# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
Unidad de aprendizaje: Algortimos Genéticos
Author: Del Angel Hernández Tania Ameyalli
Descripción:

Created on Wed May 18 18:12:42 2022

@author: tania
"""

from Individuo import Individuo

class Poblacion:

    #en el cosntructor habran los maximos y minimos que representan los valores que pueden tomar los parametros (variables: a,b,c...)
    #nbits es para el numero de particiones
    def __init__(self, size, minis, maxis, nbits):
        #self.target = target
        self.size = size
        self.nbits = nbits
        self.maxis = maxis
        self.minis = minis

    def inicializa(self):
        '''
        La poblacion se inicializa, todos los valores seran guardados en una lista.

        se van a crear individuos segun los minis, maxis y nbits que se hayan proporcionado
        se llama al metodo init de la clase individuo, ahi mismo se le asigna el cromosoma al individuo
        Terminando de crear al individuo se agrega ese individuo a la poblacion con el metodo append()
        '''
        poblacion = []
        for i in range(self.size):
            ind = Individuo(self.minis, self.maxis, self.nbits)
            ind.init()
            poblacion.append(ind)
        self.poblacion = poblacion
