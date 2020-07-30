from MH.Metaheuristica import Metaheuristica
import numpy as np
from BD.DTO.IndicadoresMH import IndicadoresMH

class Rand1Dimension(Metaheuristica):
    def __init__(self):
        self.problema = None
        self.soluciones = None
        self.parametros = {}
        print(f"Mh Rand1Dimension creada")
        

    
    def setProblema(self, problema):
        self.problema = problema

    def getProblema(self):
        return self.problema

    def generarPoblacion(self, numero):
        self.soluciones = self.problema.generarSoluciones(numero)
    
    def setParametros(self, parametros):
        for parametro in parametros:
            self.parametros[parametro.nombre] = parametro.valor
    
    def getParametros(self):
        return self.parametros

    def realizarBusqueda(self):
        print(f"parametros {self.parametros}")
        print(f"soluciones {self.soluciones}")
        self._perturbarSoluciones()
        fitness = self.problema.evaluarFitness(self.problema.decode(self.soluciones))
        minFitness = np.min(fitness)
        indicadorFitness = IndicadoresMH()
        indicadorFitness.nombre("fitness")
        indicadorFitness.valor(minFitness)
        self.indicadores = [indicadorFitness]

    def _perturbarSoluciones(self):
        idsPerturbar = np.random.randint(low=0,high=self.problema.getNumDim(), size=(self.soluciones.shape[0]))
        columnas = np.arange(self.soluciones.shape[0])
        random = np.random.uniform(low=-1,high=1,size=(self.soluciones.shape[0])) * self.parametros['salto']
        print(f"iniciales {self.soluciones}")
        self.soluciones[columnas, idsPerturbar] += random.T
        print(f"finales {self.soluciones}")