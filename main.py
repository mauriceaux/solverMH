import os
from datetime import datetime
from BD import RegistroMH
from Problema import LectorProbOpt
from MH import MHFactory
from Solver.GenericSolver import GenericSolver
from BD.DTO import EstadoExperimento
from Agente import AgenteFactory



C_PROBLEM = '.Problema/Instancias'

if __name__ == "__main__":
    inicio = datetime.now()
    cont = 0
    for _ in range(1):
        experimento = RegistroMH.obtenerExperimento()
        if experimento is None: break
        try:
            parametros = experimento.getParametros()
            problema = LectorProbOpt.leer(os.path.join(C_PROBLEM, parametros.getNomProblema(), parametros.getInstProblema()))
            mh = MHFactory.crear(parametros.getNomMh())
            mh.setProblema(problema)
            agente = AgenteFactory.crear(parametros.getNomAgente())
            agente.setParametros(parametros.getParametrosOptimizables())
            solver = GenericSolver()
            solver.setMH(mh)
            solver.setAgente(agente)
            resultado = solver.resolverProblema()
            experimento.setResultado(resultado)
            RegistroMH.guardarExperimento(experimento)
            cont += 1
        except Exception as ex:
            print(ex)
            experimento.setEstado(EstadoExperimento.PENDIENTE)
            RegistroMH.guardarExperimento(experimento)
    fin = datetime.now()
    print(f"fin, {cont} experimentos ejecutados, tiempo de ejecución: {fin-inicio}")