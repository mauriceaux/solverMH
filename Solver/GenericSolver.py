from BD.DTO.Resultado import Resultado

class GenericSolver:
    def __init__(self):
        print(f"Creando solver")
        self.mh = None
        self.agente = None
        self.numIteraciones = 100

    def setMH(self,mh):
        self.mh = mh

    def getMH(self):
        return self.mh

    def setAgente(self, agente):
        self.agente = agente

    def getAgente(self):
        return self.agente

    def resolverProblema(self):
        print(f"Resolviendo problema")
        assert self.mh is not None, "No se ha iniciado la MH"
        assert self.agente is not None, "No se ha iniciado el Agente"
        self.agente.setParametros(self.mh.getParamIniciales())
        for i in range(self.numIteraciones):
            indicadores = self.mh.aplicarBusqueda()
            paramOptimizados = self.agente.observarIndicadores(indicadores)
            self.mh.setParametros(paramOptimizados)
        resultados = Resultado()
        print(f"Problema resuelto")
        return resultados