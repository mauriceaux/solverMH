from BD.DTO.Experimento import Experimento
from BD.DTO.Parametro import Parametro

def obtenerExperimento():
    print(f"Obteniendo experimento desde la base de datos")
    parametros = Parametro()
    parametros.setNomProblema('PROBLEMA_PRUEBA')
    parametros.setInstProblema('prblm1.txt')
    parametros.setNomMh('MH_PRUEBA')
    parametros.setNomAgente('AgenteGenerico')
    paramOpt = None
    parametros.setParametrosOptimizables(paramOpt)
    experimento = Experimento()
    experimento.setParametros(parametros)
    return experimento

def guardarExperimento(experimento):
    print(f"Experimento guardado")