class Parametro:
    def __init__(self):
        print("Construyendo un conjunto de parametros")
        self.nomProblema = None
        self.instProblema = None
        self.nomMh = None
        self.nomAgente = None
        self.parametrosAgente = None
        self.parametrosMH = None
    
    def setParametrosMH(self,parametros):
        self.parametrosMH = parametros

    def getParametrosMH(self):
        return self.parametrosMH

    def setParametrosAgente(self,parametros):
        self.parametrosAgente = parametros

    def getParametrosAgente(self):
        return self.parametrosAgente

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