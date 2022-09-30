from modulos.classes import Solicitud
from funciones.date_translate import date_translate
from funciones.file_to_dic import get_consec
import os


def reescribe(dir_path, dic_import):
    """
    Función que abre un archivo y lo actualiza con los datos de un diccionario.
    argumento 1: string con el path donde está el archivo que se desea actualizar.
    argumento 2: diccionario con los datos que se desea aparezcan en el archivo actualizado.

    Se abre el archivo del argumento 1, se borra el contenido y se reescriben los datos que están en el diccionario.
    """
    archivo= open(dir_path, "a")
    diccionario= dic_import

    open(dir_path, "w").close()     #Limpiar el contenido del archivo
    if len(dic_import)==0:          #Para evitar errores al intentar crear un diccionario con claves vacías se agrega un registro de relleno
        archivo.write("000000*fecha*usuario*registro*usuario*cantidad*criptos")

    for k in diccionario.keys():    #Bucle que escribe en el archivo cada dato del diccionario seguido por un (*) para poder manipular el archivo más adelante
        archivo.write(str(k))
        for v in list(diccionario.get(k)):
            archivo.write("*" + str(v))
        archivo.write("\n")
    archivo.close()

def movimiento_cliente(usuario, list_import):
    """
    Función que abre el archivo de extractos del usuario y lo actualiza con los datos de una lista.
    argumento 1: string con el path donde está el archivo que se desea actualizar.
    argumento 2: listado con los datos que se desea aparezcan en el archivo actualizado.

    Se abre el archivo del argumento 1, se borra el contenido y se reescriben los datos que están en el listado que se importó.
    """
    archivo= open(str(os.getcwd() + "/files/extracto_" + usuario + ".txt"), "a")    #Abrir archivo de extracto del usuario
    consecutivo= get_consec(archivo.name)               #Genera el nuevo consecutivo para el registro que se va a agregar
    fecha= date_translate()                             #Traduce la fecha del sistema al español
    archivo.write("\n" + consecutivo + "*" + fecha + "*" + list_import[0] + "*" + list_import[1] + list_import[2] + "*" + list_import[3] + "*" + list_import[4] + "*USD$" + str(list_import[5])) #Escribe el registro del movimiento en el extracto del usuario
    archivo.close()