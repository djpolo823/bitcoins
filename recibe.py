#abrir archivo de usuarios registrados en la red
from extracto import mostrar_extracto
from funciones.date_translate import date_translate
from modulos.criptomonedas import consultar_cryptos
from login import usuario
from funciones.file_to_dic import file_to_dic, get_consec
from modulos.classes import Criptomoneda
import os

def recibir(arg_usuario):
    """
    Función que permite registrar una solicitud de transferencia a otro usuario de la aplicación.
    La función consulta la información de los usuarios registrados en la aplicación a quienes se les haría la solicitud.
    Genera un listado de las criptomonedas disponibles en la aplicación coinmarketcap.com.
    Verifica que el usuario ingrese el nombre y la cantidad correcta de la criptomoneda que desea solicitar.
    Agrega un registro en el archivo /files/solicitudes.txt de la solicitud realizada para que el usuario a quien se le está pidiendo que haga la transferencia lo vea cuando abra la aplicación.
    El registro también es visible desde el extracto del usuario solicitante como del usuario a quien se le hace la solicitud.
    Cuando se genere la solicitud, el usuario solicitante deberá esperar a que el usuario a quien se le hace la solicitud revise la aplicación y le de respuesta.
    """
    myself= usuario.user                                
    participantes=file_to_dic("files/usersfile.txt","*")    #Crea un diccionario con el nombre de todos los usuarios inscritos en la aplicación
    print("Estos son los usuarios inscritos a su red:\n")
    print("Código\tUsuario")
    for c in participantes.keys():                          #Para no mostrar el nombre del usuario que está usando la aplicación este condicional excluye el nombre del usuario
        if c == "":
            continue
        if c == usuario.code:
            continue
        print(c + "\t" + participantes.get(c)[0])
    solicitar=input("\nA cuál de ellos desea hacerle la solicitud?\nCódigo>")
    while not participantes.get(solicitar):                 #Bucle que valida si el código del usuario a quien se le hará la solicitud existe en el diccionario
        solicitar("Usuario no existe, intentelo de nuevo.\nCódigo>")
    #enviarle una solicitud de transferencia
    else:
        dic_criptos=consultar_cryptos()                     #Crea un diccionario con el nombre de las criptomonedas existentes en la API de coinmarketcap.com
        print("Estos son las criptomonedas disponibles para transferir:\n\n")
        print(list(dic_criptos.keys()))
        criptos= Criptomoneda("",0,"")                      #Crea una instancia de la clase Criptomoneda
        criptos.indicarnombre(input("Qué criptomoneda le solicitará a " + participantes.get(solicitar)[0] + "?\n>"))
        os.system("cls")
        while not criptos.nombre in list(dic_criptos.keys()):   #Valida que la criptomoneda existe en el listado
            criptos.indicarnombre(input("Criptomoneda no encontrada en el listado de criptomonedas disponibles.  \nIntente de nuevo:\n>"))
        else:                                               #En caso de que la criptomoneda si este en el diccionario
            criptos.indicarsaldo(int(input("Qué cantidad de " + criptos.nombre + " desea pedirle a " + participantes.get(solicitar)[0] + "?\n>")))
            while criptos.saldo <=0 or not isinstance(criptos.saldo, int):  #Valida que la cantidad solicitada sea valida
                criptos.indicarsaldo("El valor ingresado no es valido.  Intente de nuevo.\n¿Qué cantidad de " + criptos.nombre + " desea pedirle a " + participantes.get(solicitar)[0] + "?\n>")
            path_name=os.getcwd()                           #Guarda la ubicación actual del archivo para usarla como parametro más adelante
            archivo_solicitudes=open((path_name + "/files/solicitudes.txt"),"a")    #Abre el archivo /files/solicitudes.txt
            consecutivo = get_consec(archivo_solicitudes.name)  #Consigue el número de consecutivo que sigue en el archivo /files/solicitudes.txt                       
            fecha=date_translate()                          #Traduce la fecha del sistema al español
            archivo_solicitudes.write("\n" + consecutivo + "*" + fecha + "*" + myself + usuario.code + "*solicita "+ participantes.get(solicitar)[0] + "*" + str(criptos.saldo) + "*" + criptos.nombre) #Registra la solicitud en el archivo /files/solicitudes.txt del usuario a quien se le hace la solicitud
            archivo_solicitudes.close()
            archivo_usuario=open((path_name + "/files/extracto_" + myself + usuario.code + ".txt"), "a")    #Abre el archivo de extracto del usuario
            consecutivo= get_consec(archivo_usuario.name)   #Consigue el consecutivo en el archivo de extracto
            fecha=date_translate()                          #Traduce la fecha del sistema al español
            archivo_usuario.write("\n" + consecutivo + "*" + fecha + "*solicitud de transferencia a " + participantes.get(solicitar)[0] + solicitar + "*" + str(criptos.saldo) + "*" + criptos.nombre + "*" + dic_criptos.get(criptos.nombre)[1] + "*")  #Registra la solicitud en el archivo de extracto del usuario quien haría la transferencia
            archivo_usuario.close()
            archivo_usuario=open((path_name + "/files/extracto_" + participantes.get(solicitar)[0] + solicitar + ".txt"), "a")
            consecutivo= get_consec(archivo_usuario.name)   #Consigue el consecutivo en el archivo de extracto
            archivo_usuario.write("\n" + consecutivo + "*" + fecha + "*solicitud_de_transferencia_de " + myself + usuario.code + "*" + str(criptos.saldo) + "*" + criptos.nombre + "*" + dic_criptos.get(criptos.nombre)[1] + "*")   #Registra la solicitud en el archivo de extracto del usuario a quien se le hace la solicitud
            archivo_usuario.close()
            input("El usuario " + participantes.get(solicitar)[0] + " recibió su solicitud, ahora debe esperar que " + participantes.get(solicitar)[0] + " le de respuesta.")

#esperar respuesta
#En caso de aprobación recibir la transferencia
#aumentar el saldo