class ParametroAgente:
    def __init__(self):
        self.tipo = None
        self.paso = None
        self.minimo = None
        self.maximo = None
        self.componente = None
        self.valorInicial = None
        print(f"ParametroAgente creado")

    def setValorInicial(self, valorInicial):
        self.valorInicial = valorInicial

    def getValorInicial(self):
        return self.valorInicial

    def setTipo(self, tipo):
        self.tipo = tipo

    def getTipo(self):
        return self.tipo

    def setPaso(self, paso):
        self.paso = paso

    def getPaso(self):
        return self.paso

    def setMinimo(self, minimo):
        self.minimo = minimo

    def setMaximo(self, maximo):
        self.maximo = maximo

    def getMaximo(self):
        return self.maximo

    def setComponente(self, componente):
        self.componente = componente

    def getComponente(self):
        return self.componente