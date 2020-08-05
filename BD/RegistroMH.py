from DTO.Experimento import Experimento
from DTO.Parametro import Parametro
from DTO.ParametroAgente import ParametroAgente
from DTO.ParametroMH import ParametroMH
from DTO import TipoDominio, TipoComponente

from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
import configparser
import json
from collections import namedtuple

config = configparser.ConfigParser()
config.read('BD/conf/db_config.ini')
host = config['postgres']['host']
db_name = config['postgres']['db_name']
port = config['postgres']['port']
user = config['postgres']['user']
pwd = config['postgres']['pass']

engine = create_engine(f'postgresql://{user}:{pwd}@{host}:{port}/{db_name}')

sqlObtenerExp  = "update datos_ejecucion set estado = 'ejecucion', inicio = :inicio "
sqlObtenerExp += "where id =  "
sqlObtenerExp += "(select id from datos_ejecucion "
sqlObtenerExp += "    where estado = 'pendiente' "
sqlObtenerExp += "    and nombre_algoritmo = :nombre "
sqlObtenerExp += "    order by id asc "
sqlObtenerExp += "    limit 1) returning id, parametros;"

def insertDummyExp(nombreExperimento):
    sqlInsert = "INSERT INTO datos_ejecucion(nombre_algoritmo, parametros, estado) VALUES (:nomExp, :param, 'pendiente')"
    parametros = Parametro()
    parametros.setNomProblema("Esfera")
    #parametros.setInstProblema(paramBD.nomInstProblema)
    parametros.setNomMH("Rand1Dimension")
    parametros.setNomAgente("AgenteGenerico")
    paramsMH = {}
    saltoStr = "salto"
    paramsMH[saltoStr] = 2
    paramsMH["poblacion"] = 4
    paramsMH["numIter"] = 1000
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
    session = createSession()
    session.execute(sqlInsert,{
        "nomExp":nombreExperimento
        , "param": json.dumps(parametros.__dict__, default=lambda o: o.__dict__) 
        })
    session.commit()

def createSession():
    return sessionmaker(bind=engine)()

def obtenerExperimento(nombreExperimento):
    print(f"Obteniendo experimento desde la base de datos")
    session = createSession()
    inicio = datetime.now()
    arrResult = session.execute(sqlObtenerExp,{"inicio":inicio, "nombre": nombreExperimento}).fetchone()
    session.commit()
    if arrResult is None: return None
    paramBD = json.loads(arrResult.parametros, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    parametros = Parametro()
    parametros.setNomProblema(paramBD.nomProblema)
    #parametros.setInstProblema(paramBD.nomInstProblema)
    parametros.setNomMH(paramBD.nomMH)
    parametros.setNomAgente(paramBD.nomAgente)
    parametros.setParametrosMH(paramBD.parametrosMH._asdict())
    paramsAgente = []
    for pAgente in paramBD.parametrosAgente:
        param = ParametroAgente(pAgente)
        paramsAgente.append(param)
    parametros.setParametrosAgente(paramsAgente)
    experimento = Experimento()
    experimento.setParametros(parametros)
    experimento.setId(arrResult.id)
    return experimento

def guardarExperimento(experimento, inicio, fin):
    session = createSession()
    metadata = db.MetaData()
    resultadoEjecucion = db.Table('resultado_ejecucion', metadata, autoload=True, autoload_with=engine)
    datosEjecucion = db.Table('datos_ejecucion', metadata, autoload=True, autoload_with=engine)
    insertResultadoEjecucion =resultadoEjecucion.insert()
    updateDatosEjecucion = datosEjecucion.update().where(datosEjecucion.c.id == experimento.getId())
    if experimento.getResultado() is not None:
        session.execute(insertResultadoEjecucion, {
                    'id_ejecucion':experimento.getId()
                    ,'fitness' : experimento.getResultado().getFitness()
                    ,'inicio': inicio 
                    ,'fin': fin
                    ,'mejor_solucion' : experimento.getResultado().getMejorSolucion()
                    })
    session.execute(updateDatosEjecucion, {
        "fin": fin
        ,"estado": experimento.getEstado()
    })
    session.commit()
    print(f"Experimento guardado")

def guardaDatosIteracion(data):
    if data is None:
        print(f"Nada que guardar!")
        exit()
    session = createSession()
    metadata = db.MetaData()
    datosIteracion = db.Table('datos_iteracion', metadata, autoload=True, autoload_with=engine)
    insertDatosIteracion = datosIteracion.insert()
    session.execute(insertDatosIteracion, data)
    session.commit()