class Parametro:
    def __init__(self):
        print("Construyendo un conjunto de parametros")
        self.nomProblema = None
        self.instProblema = None
        self.nomMh = None
        self.nomAgente = None
        self.parametrosOptimizables = None
    
    def setParametrosOptimizables(self,parametros):
        self.parametrosOptimizables = parametros

    def getParametrosOptimizables(self):
        return self.parametrosOptimizables

    def setNomProblema(self,nomProblema):
        self.nomProblema = nomProblema

    def getNomProblema(self):
        return self.nomProblema

    def setInstProblema(self,instProblema):
        self.instProblema = instProblema

    def getInstProblema(self):
        return self.instProblema

    def setNomMh(self,nomMh):
        self.nomMh = nomMh

    def getNomMh(self):
        return self.nomMh

    def setNomAgente(self,nomAgente):
        self.nomAgente = nomAgente

    def getNomAgente(self):
        return self.nomAgente