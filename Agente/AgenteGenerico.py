class AgenteGenerico:
    def __init__(self):
        self.parametros = None
        print(f"Instancia de agente generico creada")

    def setParametros(self, parametros):
        self.parametros = parametros

    def getParametros(self):
        return self.parametros
    
    def observarIndicadores(self,indicadores):
        print(f"Indicadores observados")
        return self.getParametros()
    
    #def optimizarParametrosMH(self):
