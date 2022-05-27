# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
Unidad de aprendizaje: Algortimos Genéticos
Author: Del Angel Hernández Tania Ameyalli
Descripción:

Created on Wed May 18 18:15:35 2022

@author: tania
"""

import numpy as np
import random
class Seleccion:

    '''
    Se hace la seleccion de los nuevos individuos conforme a sus aptitudes
    Nota: Se le da preferencia a los individuos con mayor aptitud, pero si alguno tiene aptitud baja, tiene posibilidad de ser elegido, por eso se agrega un pequeño valor (.01)

    Se calcula la probabilidad de ser elegido mediante la funcion de softmax, la cual saca la probabilidad de un individuo según su aptitud.

    esas probabilidades de guardan en una lista y para finalizar se sacan los indices de esas probabilidades y se devuelve el indice de donde esta guardado el individuo y la probabilidad de ser elegido
    '''


    def selecciona(self, aptitudes, k=2):
        # Darle chance a los feos
        aptitudes = np.array(aptitudes) + .01
        #Por cada individuo que tenga mejor aptitud se regresa dicho individuo
        #para darle prioridad
        probabilidades = [np.exp(aptitud)/np.sum(np.exp(aptitudes))
                  for aptitud
                  in aptitudes]
        indices = list(range(len(aptitudes)))
        return random.choices(indices, probabilidades, k=k)
