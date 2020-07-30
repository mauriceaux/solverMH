from Problema.Problema import Problema
import numpy as np

class Esfera(Problema):
    def __init__(self):
        self.numDimensiones = 2
        self.dominioDimensiones = np.array([[-100,-100],[100,100]])
        print(f"Problema esfera creado")

    def getNombre(self):
        return "Esfera"

    def setNumDim(self, num):
        self.numDimensiones = num
    
    def getNumDim(self):
        return self.numDimensiones

    def setDominioDim(self, dominio):
        self.dominioDimensiones = dominio
    
    def getDominioDim(self):
        return self.dominioDimensiones

    def generarSoluciones(self, numero):
        res = []
        for i in range(self.getNumDim()):
            res.append(np.random.uniform(low=self.getDominioDim()[0,i], high=self.getDominioDim()[1,i], size=(numero)))
                
        return np.array(res).T