from DTO.Resultado import Resultado
from DTO import TipoIndicadoresMH
import json
from BD import RegistroMH
from datetime import datetime

class GenericSolver:
    def __init__(self):
        print(f"Creando solver")
        self.mh = None
        self.agente = None
        self.numIterGuardar = 20

    def setMH(self,mh):
        self.mh = mh

    def getMH(self):
        return self.mh

    def setAgente(self, agente):
        self.agente = agente

    def getAgente(self):
        return self.agente

    def resolverProblema(self, idExperimento):
        print(f"Resolviendo problema")
        assert self.mh is not None, "No se ha iniciado la MH"
        assert self.agente is not None, "No se ha iniciado el Agente"

        self.mh.generarPoblacion(self.mh.getParametros()["poblacion"])
        resultadosIter = []
        for i in range(self.mh.getParametros()["numIter"]):
            inicio = datetime.now()
            self.mh.realizarBusqueda()
            indicadores = self.mh.getIndicadores()
            self.agente.observarIndicadores(indicadores)
            paramOptimizadosMH = self.agente.optimizarParametrosMH()
            paramOptimizadosProblema = self.agente.optimizarParametrosProblema()
            self.mh.setParametros(paramOptimizadosMH)
            self.mh.problema.setParametros(paramOptimizadosProblema)
            fin = datetime.now()
            data = {
                "id_ejecucion": idExperimento
                ,"numero_iteracion": i
                ,"fitness_mejor": indicadores[TipoIndicadoresMH.FITNESS_MEJOR_GLOBAL]
                ,"fitness_promedio": indicadores[TipoIndicadoresMH.FITNESS_PROMEDIO]
                ,"fitness_mejor_iteracion": indicadores[TipoIndicadoresMH.FITNESS_MEJOR_ITERACION]
                ,"parametros_iteracion": json.dumps({"paramAgente": json.dumps(self.agente.getParametros())
                                            ,"paramMH": json.dumps(self.mh.getParametros())
                                            ,"paramProblema": json.dumps(self.mh.problema.getParametros())
                                            })
                ,"inicio": inicio
                ,"fin": fin
                ,"datos_internos": None
            }
            resultadosIter.append(data)
            if i % self.numIterGuardar == 0:
                RegistroMH.guardaDatosIteracion(resultadosIter)                
                resultadosIter = []
            print(f"Mejor fitness {self.mh.problema.getMejorEvaluacion()}\tmejora acumulada {self.agente.mejoraAcumulada}")
        if len(resultadosIter) > 0:
            RegistroMH.guardaDatosIteracion(resultadosIter)
        resultados = Resultado()
        resultados.setFitness(self.mh.problema.getMejorEvaluacion())
        resultados.setMejorSolucion(json.dumps(self.mh.soluciones[self.mh.idxMejorSolucion].tolist()))
        print(f"Problema resuelto, mejor fitness {self.mh.problema.getMejorEvaluacion()}")
        return resultados