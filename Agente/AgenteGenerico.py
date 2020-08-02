from DTO import TipoIndicadoresMH, TipoParametro, TipoComponente, TipoIndicadoresMH
import numpy as np

class AgenteGenerico:
    def __init__(self):
        self.parametros = None
        self.indiceMejora = 0
        self.mejoraAcumulada = 0
        print(f"Instancia de agente generico creada")

    def setParametros(self, parametros):
        self.parametros = parametros

    def getParametros(self):
        return self.parametros
    
    def observarIndicadores(self,indicadores):
        self.indiceMejora = indicadores[TipoIndicadoresMH.INDICE_MEJORA]
        self.mejoraAcumulada += indicadores[TipoIndicadoresMH.INDICE_MEJORA]
        
        
    
    def optimizarParametrosMH(self):
        ret = {}
        for parametro in self.parametros:
            if (self.mejoraAcumulada < 0 
                and parametro.getComponente() == TipoComponente.METAHEURISTICA):
                if parametro.getTipo() == TipoParametro.CONTINUO :
                    ret[parametro.getNombre()] = np.random.uniform(low=parametro.getMinimo(),high=parametro.getMaximo())
                if parametro.getTipo() == TipoParametro.DISCRETO :
                    ret[parametro.getNombre()] = np.random.randint(low=parametro.getMinimo(),high=parametro.getMaximo()+1)
        return ret

    def optimizarParametrosProblema(self):
        ret = {}
        for parametro in self.parametros:
            if (self.mejoraAcumulada < 0.01 
                and parametro.getComponente() == TipoComponente.PROBLEMA):
                if parametro.getTipo() == TipoParametro.CONTINUO :
                    ret[parametro.nombre] = np.random.uniform(low=parametro.getMinimo(),high=parametro.getMaximo())
                if parametro.getTipo() == TipoParametro.DISCRETO :
                    ret[parametro.nombre] = np.random.randint(low=parametro.getMinimo(),high=parametro.getMaximo()+1)
        return ret

