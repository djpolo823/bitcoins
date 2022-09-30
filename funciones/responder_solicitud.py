from modulos.classes import Solicitud
from funciones.date_translate import date_translate
from funciones.file_to_dic import get_consec
import os

def rechazar_transferencia(dic_pend, class_solicitud, codigo_usuario):
    os.system("cls")
    print("Ha rechazado la transacción número " + str(class_solicitud.consecutivo))
    dic_pend.pop(class_solicitud.consecutivo)
    archivo=str(os.getcwd() + "/files/solicitudes.txt")
    open(archivo, "w").close()
    archivo_solicitudes=open(archivo, "r+")
    if len(dic_pend)==0:
        archivo_solicitudes.write("000000*fecha*admon*apertura*admon*cantidad*criptos")
    for k in dic_pend.keys():
        archivo_solicitudes.write(str(k))
        for v in list(dic_pend.get(k)):
            archivo_solicitudes.write("*" + str(v))
        archivo_solicitudes.write("\n")
    archivo_solicitudes.close()
    archivo=str(os.getcwd() + "/files/extracto_" + class_solicitud.a_quien + codigo_usuario+ ".txt")
    print("Propio:\t" + archivo)
    archivo_usuario=open(archivo, "a")
    consecutivo=get_consec(archivo_usuario.name)
    fecha=date_translate()
    archivo_usuario.write("\n" + str(consecutivo) + "*" + fecha + "*solicitud rechazada a " +  str(class_solicitud.solicitante) + "*" + str(class_solicitud.cantidad) + "*" + class_solicitud.criptomoneda)
    archivo_usuario.close()
    archivo=str(os.getcwd() + "/files/extracto_" + class_solicitud.solicitante + ".txt")
    print("Destinatario:\t" + archivo)
    archivo_usuario=open(archivo, "a")
    consecutivo=get_consec(archivo_usuario.name)
    fecha=date_translate()
    archivo_usuario.write("\n" + consecutivo + "*" + fecha + "*solicitud de transferencia rechazada por " + class_solicitud.a_quien + " de*" + class_solicitud.cantidad + "*" + class_solicitud.criptomoneda)
    archivo_usuario.close()