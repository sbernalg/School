import numpy as np
class FitnessFunction:

    def __init__(self, resultado, coefic):
        #TARGET es el resultado a encontrar
        self.target = resultado
        self.lamda = 1
        self.beta = 1
        self.coeficientes = coefic

    def evaluate(self, ind):
        '''
        Evalua la aptitud de un individuo
        Parameters
        ----------
        ind : Individuo
            DESCRIPTION. Representa una
            solucion posible

        Returns
        -------
        int
            DESCRIPTION. Aptitud del
            individuo es que tan cerca estuvo de resolver la ecuación
            '''


        variables = ind.cromosoma.getValues()
        #Se obtiene la lista de los coeficientes
        coef = self.coeficientes
        #Se hace un producto punto
        act = np.dot(variables, coef)
        #lo que sale es lo que da la solucion encontrada a eso se le resta el resultado que deberia de encontrarse y se hace uso de e para retornar la actitud
        x = np.abs(self.target - act)
        return self.beta*np.exp(-self.lamda * x)
