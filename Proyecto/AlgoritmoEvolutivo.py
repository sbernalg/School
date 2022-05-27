# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
Unidad de aprendizaje: Algortimos Genéticos
Author: Del Angel Hernández Tania Ameyalli
Descripción:

Created on Wed May 18 18:22:40 2022

@author: tania
"""

"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM Zumpango

Unidad de Aprendizaje: Algoritmos genéticos

Alumno: del Angel Hernández Tania Ameyalli

Descripción:  Algoritmo genético V1.0

Created on Mon Mar  7 12:48:33 2022

@author: asdruballopezchau
"""

import numpy as np
import random
from Individuo import Individuo
from Poblacion import Poblacion
from FitnessFunction import FitnessFunction
from Seleccion import Seleccion
from collections import OrderedDict

class AlgoritmoEvolutivo:

    def __init__(self, size, target, minis, maxis, nbits, coefic):

        '''
        Recibe el volumen, el tamaño de la poblacion y conforme, nbits sera el tamaño de cada individuo
        '''
        self.size = size
        self.pob = None
        self.target = target
        self.minis = minis
        self.maxis = maxis
        self.nbits = nbits
        #coeficientes representa los coeficientes de la ecuacion
        self.coeficientes = coefic

    def showPob(self, showAptitude=False):
        '''
        Si showAptitude es verdadero va a mostrar al individuo y la aptitud que tenga ese individuo, los individuos son sacados de la poblacion
        '''

        if showAptitude:
            aptitudes = [self.ff.evaluate(ind)
                     for ind in self.pob.poblacion]

        for i in range(self.size):
            if showAptitude:
                print(self.pob.poblacion[i].cromosoma.getValues() ,
                      "Con aptitud -> " + str(aptitudes[i]))

            else:
                print(self.pob.poblacion[i])

    def showElite(self):
        aptitudes = [self.ff.evaluate(ind)
                 for ind in self.pob.poblacion]

        idxMejor = np.argmax(aptitudes)
    #
    #     print("El de mejor aptitud fue: ", self.pob.poblacion[idxMejor].__str__(), "con aptitud: ", aptitudes[mayAp])
    # #     pass
        return self.pob.poblacion[idxMejor]

    def inicializa(self):
        #Crea e icializa la población
        pob = Poblacion(self.size, self.minis, self.maxis, self.nbits)
        pob.inicializa()
        self.pob = pob
        #Crea un objeto de tipo Seleccion
        self.seleccion = Seleccion()
        #Crea un objeto de tipo FitnessFunction
        self.ff = FitnessFunction(self.target, self.coeficientes)


    def evolucion(self):
        # 1) Evaluar individuos
        # 2) Seleccionar padres para cruza
        # 3) Generar hijos (cruza)
        # 4) Mutar a algunos
        # 5) Evaluar hijos
        # 6) Seleccionar miembros de la siguiente población
        ####### Implementación #############
        if self.pob is None:
            print("Inicialice la población")
            return
        #1) Evaluar individuos

        '''
        Mediante el metodo ff de la clase fitnessfunction se va a sacar la aptitud de la poblacion inicial
        '''

        poblacion = self.pob.poblacion
        aptitudes = [self.ff.evaluate(ind)
                     for ind in poblacion]
        # # 2) Seleccionar padres para cruza
        '''
        Se va a dividr la poblacion a la mitad y de esa mitad se va a escoger a los padres, en este caso de van a escoger primero a los padres con mejor aptitud, para ello se manda a llamar al metodo selecciona de la clase seleccion
        '''
        k = int(self.size/2)
        if k%2 == 1:
            k += 1
        idx = self.seleccion.selecciona(aptitudes,
                                  k)
        #3) Generar hijos (cruza)

        '''
        Se va a crear una lista donde se va a guardar a los hijos, aqui se manda a llamar al metodo cruza del la clase individuo para hacer la cruza, mediante los padres elegidos, se va tomar la mitad de los genes de uno y de otro, variando entre que mitad de genes se van a escoger

        se unen las mitades escogidas y con eso generamos a los hijos, los guardamos en la lista llamada descendencia
        '''

        descendencia = []
        for i in list(range(0,k-1,2)):
            ip = idx[i]
            im = idx[i+1]
            papa = poblacion[ip]
            mama = poblacion[im]
            hijos = papa.cruza(mama)
            descendencia.append(hijos[0])
            descendencia.append(hijos[1])

        # 4) Mutar a algunos (5%)
        '''
        Sacamos el procentaje de individuos que sevan a mutar de la lista descendencia

        vamos a escoger los individuos que vamos a mutar y vamos a mutar los individuos escogidos segun el indice que sacamos y el indice que tengan en la lista
        '''
        totalMutar = int(np.ceil(len(descendencia)*0.1))

        for i in range(totalMutar):
            idx = random.choice(range(len(descendencia)))
            descendencia[idx].mutar()
        # 5) Evaluar hijos
        # 6) Seleccionar miembros de la siguiente
        #     población

        # Junto padres e hijos
        '''
        Colocamos a los hijos en la lista poblacion para que hijos y padres esten juntos
        '''

        for hijo in descendencia:
            poblacion.append(hijo)
        # calculo aptitudes de todos
        '''
        Sacamos la aptitud de todos
        '''
        aptitudes = [self.ff.evaluate(ind)
                     for ind in poblacion]
        # ELITISMO!!!!!
        '''
        Se saca el indice de la mejor aptitud de la lista aptitudes, y esa se ira a la lista llamada siguientePob
        '''
        idxMejor = np.argmax(aptitudes)
        # El mejor pasa directamente a la siguiente población
        siguientePob = []
        siguientePob.append(poblacion[idxMejor])
        # Selecciono indices de
        # individuos para la siguiente generacion
        '''
        Segun las aptitudes de la de los individuos (sin tener en cuenta al que mejor aptitud tuvo ya que ese paso directo ala nueva generacion) se va a llamar al metodo selecciona de la clase seleccion, para así escoger a los individuos segun su probabilidad de ser elegidos.
        '''
        idx = self.seleccion.selecciona(aptitudes,
                                  self.size)
        # Creo la lista de individuos de la siguiente
        # generación

        for i in idx:
            siguientePob.append(poblacion[i])
        # Guardo para la siguiente evolución
        self.pob.poblacion = siguientePob
