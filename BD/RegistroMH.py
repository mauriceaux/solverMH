from DTO.Experimento import Experimento
from DTO.Parametro import Parametro
from DTO.ParametroAgente import ParametroAgente
from DTO.ParametroMH import ParametroMH
from DTO import TipoDominio, TipoComponente

def obtenerExperimento():
    print(f"Obteniendo experimento desde la base de datos")
    parametros = Parametro()
    parametros.setNomProblema('Esfera')
    #parametros.setInstProblema('prblm1.txt')
    parametros.setNomMh('Rand1Dimension')
    parametros.setNomAgente('AgenteGenerico')
    paramsMH = {}
    saltoStr = "salto"
    paramsMH[saltoStr] = 2
    paramsMH["poblacion"] = 4
    paramsMH["numIter"] = 1000
    #saltoInicialMH = ParametroMH()
    #saltoInicialMH.setNombre("salto")
    #saltoInicialMH.setValor(2)
    #poblacionMH = ParametroMH()
    #poblacionMH.setNombre("poblacion")
    #poblacionMH.setValor(3)
    #numIterMH = ParametroMH()
    #numIterMH.setNombre("numIter")
    #numIterMH.setValor(10)
    #paramsMH.append(saltoInicialMH)
    #paramsMH.append(poblacionMH)
    #paramsMH.append(numIterMH)
    parametros.setParametrosMH(paramsMH)
    paramsAgente = []
    salto = ParametroAgente()
    salto.setNombre(saltoStr)
    salto.setTipo(TipoDominio.CONTINUO)
    salto.setMinimo(1)
    salto.setMaximo(10)
    salto.setComponente(TipoComponente.METAHEURISTICA)
    paramsAgente.append(salto)
    parametros.setParametrosAgente(paramsAgente)
    experimento = Experimento()
    experimento.setParametros(parametros)
    return experimento

def guardarExperimento(experimento):
    print(f"Experimento guardado")