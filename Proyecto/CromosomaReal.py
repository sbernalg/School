# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
Unidad de aprendizaje: Algortimos Genéticos
Author: Del Angel Hernández Tania Ameyalli
Descripción:

Created on Wed May 18 18:09:05 2022

@author: tania
"""
#Importamos GenReal ya que un cromosoma esta compuesto por varios Genes
#Cada gen representa un valor de 'x' (variable o incognita) a encontrar en la
#ecuacion lineal
from GenReal import GenReal as GR


class CromosomaReal:
    #El cromosoma recibi los minis y maxis que representan los valores
    #Mínimos y Máximos que puede tener un gen
    def __init__(self, minis, maxis, nbits):
        #Si las listas de minis y maxis no tienen la misma longitud entonces
        #termina el programa
        if len(minis)!= len(maxis):
            return
        self.minis = minis.copy()
        self.maxis = maxis.copy()
        self.nbits = nbits
        self.genes = []
        #Se crean los genes necesarios para el cromosoma
        for min, max, nb in zip(minis, maxis,nbits):
            gen= GR(min, max, nb)
            self.genes.append(gen)

    def init(self):
        #Se inicializan los genes, es decir, se les da un valor
        for gen in self.genes:
            gen.initGen()

    def cruzar(self, madre):
        #Cruza de padre y madre
        genesHijos1 = []
        genesHijos2 = []

        #Se hace uso de la cruza de GenReal para cada gen del cromosoma
        for papa, mama in zip(self.genes, madre.genes):
            hijos = papa.cruzar(mama)
            genesHijos1.append(hijos[0])
            genesHijos2.append(hijos[1])

        #Se crean dos hijos de tipo CromosomaReal
        h1 = CromosomaReal(self.minis, self.maxis, self.nbits)
        h2 = CromosomaReal(self.minis, self.maxis, self.nbits)

        #Se les asigna genes a los cromosomas creadp
        h1.genes =  genesHijos1
        h2.genes = genesHijos2

        #Se devuelven los hijos creados de la cruza
        return [h1, h2]

    def mutar(self):
        #Se hace uso de la mutacion de GenReal para cada gen del cromosoma
        #Que no es otra cosa mas que cambiar el valor del gen
        for gen in self.genes:
            gen.mutar()

    def getValues(self):
        #Por cada gen del cromosoma se obtiene su valor deciml ya que se
        #encuentra en base binaria
        valores = []
        for gen in self.genes:
            valores.append(gen.getValue())

        #Se rergesan los valores en BASE 10 obtenidos
        return valores

    def __str__(self):
        cad = ""
        for gen in self.genes:
            cad = cad + gen.__str__()
        return cad
