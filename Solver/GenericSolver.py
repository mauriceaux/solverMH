from DTO.Resultado import Resultado
from DTO import TipoIndicadoresMH
import json

class GenericSolver:
    def __init__(self):
        print(f"Creando solver")
        self.mh = None
        self.agente = None

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

        self.mh.generarPoblacion(self.mh.getParametros()["poblacion"])
        
        for i in range(self.mh.getParametros()["numIter"]):
            self.mh.realizarBusqueda()
            indicadores = self.mh.getIndicadores()
            self.agente.observarIndicadores(indicadores)
            paramOptimizadosMH = self.agente.optimizarParametrosMH()
            paramOptimizadosProblema = self.agente.optimizarParametrosProblema()
            self.mh.setParametros(paramOptimizadosMH)
            self.mh.problema.setParametros(paramOptimizadosProblema)
            print(f"Mejor fitness {self.mh.problema.getMejorEvaluacion()}\tmejora acumulada {self.agente.mejoraAcumulada}")
        resultados = Resultado()
        resultados.setFitness(self.mh.problema.getMejorEvaluacion())
        resultados.setMejorSolucion(json.dumps(self.mh.soluciones[self.mh.idxMejorSolucion].tolist()))
        print(f"Problema resuelto, mejor fitness {self.mh.problema.getMejorEvaluacion()}")
        return resultados