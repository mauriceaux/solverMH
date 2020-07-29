class Experimento:
    def __init__(self):
        print("Construyendo un experimento")
        self.parametros = None
        self.resultado = None

    def setParametros(self,parametros):
        self.parametros = parametros

    def getParametros(self):
        return self.parametros

    def setResultado(self,resultado):
        self.resultado = resultado

    def getResultado(self):
        return self.resultado

    def setEstado(self, estado):
        self.estado = estado

    def getEstado(self):
        return self.estado
    