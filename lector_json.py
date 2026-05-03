import os
import json

class Lector(object):
    def __init__(self, ruta : str = ''):
        """
        DocString of constructor:
        -------------------------
        Valida la existencia del archivo.
        """
        if ruta == '':
            raise Exception('Debe Poner una ruta')
        elif not os.path.exists(ruta):
            raise Exception('Ruta no existe')
        elif not os.path.isfile(ruta):
            raise Exception('Debe ser un archivo no un directorio')
        elif not ruta.endswith('.json'):
            raise TypeError('Debe ser un archivo .json')
        
        self.ruta = ruta

    
    def validar_contra(self, user : str, password : str) -> bool:
        """
        Docstring of "validar_contra":
        ------------------------------
        Permite validar la contraseña.
        Este tiene como argumentos el user (nombre) y 
        la password (contraseña).
        """
        with open(self.ruta,"r") as f:
            listado : list = json.load(f)

        for person in listado:
            if person.get("usuario") == user:
                if person.get("contra") == password:
                    return True
        return False
                
