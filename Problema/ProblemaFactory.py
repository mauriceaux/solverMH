import importlib

def crear(nombreProblema):
    print(f"Creando instancia de Problema: {nombreProblema}")
    
    module = importlib.import_module(f"Problema.{nombreProblema}")
    class_ = getattr(module, nombreProblema)
    return class_()