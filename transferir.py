import os

from funciones.actualiza_archivos import reescribe
from funciones.date_translate import date_translate
from funciones.file_to_dic import file_to_dic, get_consec
from funciones.modifica_saldo import comprar_criptos, transfiere_criptos
from funciones.reg_to_dic import traduce_reg_a_dic
from funciones.responder_solicitud import rechazar_transferencia
from login import usuario
from modulos.classes import Solicitud
from modulos.criptomonedas import consultar_cryptos


def transferencia(myself):
    """
    Función que permite al usuario realizar una tranferencia a otro usuario.  Las transferencias pueden realizarse a través de una solicitud hecha por otro usuario o por iniciativa propia del usuario
    Ésta función evalúa si el saldo del usuario es suficiente para realizar una transferencia, en caso de que no tenga saldo suficiente, le permite al usuario comprar criptomonedas para aumentar su saldo.
    La información del saldo del usuario la obtiene del archivo /files/usersfile.txt y actualiza las cotizaciones en USD de las criptomonedas que tiene en su saldo a través de la API  de coinmarketcap.com.
    El usuario al ingresar a la opción de tranferir podrá ver un listado de las solicitudes de trasferencia que le han hecho otros usuarios, puede elegir del listado la solicitud que desea contestar y puede aceptar las solicitudes o rechazarlas.
    Las solicitudes contestadas, se registran en el extracto del usuario, en el extracto del solicitante, en el archivo de solicitudes y en el archivo de usuarios con sus respectivos saldos.

    Ésta función recibe el argumento de tipo string donde se informa el código del usuario actual.
    """
    solicitud= Solicitud("","","","","","","")                  #Instancia de clase Solicitud usada para guardar información de las solicitudes de transferencia hechas por un usuario
    myself=usuario.user                                         
    dic_pendientes={}                                           #Diccionario creado para traer a la función todas las solicitudes pendientes registradas en el archivo /files/solicitudes.txt
    dic_solicitudes=file_to_dic("files/solicitudes.txt","*")    #Diccionario creado para traer todas las solicitudes 

    for v in dic_solicitudes.keys():                            #Bucle que separa las solicitudes pendientes y las solicitudes aprobadas o crechazadas en los dos diccionarios dispuestos para estos datos
        if v == "":
            continue
        if dic_solicitudes.get(v)[2][9:len(dic_solicitudes.get(v)[2])]==myself and dic_solicitudes.get(v)[2][0:8]=="solicita": #Condicional que extrae los registros que coinciden con el nombre del usuario y los que dicen "solicita"
            dic_pendientes.setdefault(v)                        #Guarda en dic_pendientes las solicitudes pendientes
            dic_pendientes[v]=dic_solicitudes.get(v)
    for b in dic_pendientes.keys():
        dic_solicitudes.pop(b)                                  #Borra de dic_solicitudes las solictudes que se pasaron al dic_pendientes
    
    if len(dic_pendientes)>=1:                                  #Muestra las solicitudes pendientes por aprobar hechas al usuario
        responder=input("Usted tiene " + str(len(dic_pendientes)) + " solicitudes pendientes por contestar.\n ¿Desea contestarlas ahora?\nY/N>").upper()
        os.system("cls")
        if responder=="Y":
            for sp in dic_pendientes.keys():                    #Cuándo hay una sola solicitud, ésta se guarda directamente en el objeto de tipo "solicitud"
                s=list(dic_pendientes.get(sp))                  #Traduce los datos del diccionario a una lista iterable
                solicitud.consecutivo_input(sp)
                solicitud.fecha_input(s[0])
                solicitud.solicitante_input(s[1])
                solicitud.estado_input(s[2][0:8])
                solicitud.a_quien_input(s[2][9:len(s[2])])
                solicitud.cantidad_input(s[3])
                solicitud.criptomoneda_input(s[4])
                
                print(solicitud.consecutivo + ".\t" + solicitud.fecha + "\n\t" + solicitud.solicitante[0:len(solicitud.solicitante)-4] + " le solicitó " + str(solicitud.cantidad) + " " + solicitud.criptomoneda + "\n")
            print("\nSu saldo actual es:")
            usuario.registro_input(traduce_reg_a_dic(usuario.registro))
            for saldo in usuario.registro:
                print(str(saldo) + ":\t" + '{:,.2f}'.format(usuario.registro.get(saldo)))

            if len(dic_pendientes)<2:                           #Cuándo hay solo una solicitud pendiente
                responder=input("Desea aprobar la transferencia?\nY/N>").upper()
            else:
                solicitud.consecutivo_input("")                 #Cuándo hay más de una solicitud pendiente
                responder=input("Desea aprobar una de estas transferencias?\nY/N>").upper()
                solicitud.consecutivo_input(input("Digite el consecutivo de la solicitud a la que desea darle trámite:\n>"))
            
                while str(solicitud.consecutivo) not in dic_pendientes.keys():  #Bucle que valida si el número de solicitud digitada por el usuario existe en el diccionario de solicitudes pendientes
                    solicitud.consecutivo_input(input("Consecutivo no encontrado.  Intentelo nuevamente o digite 'Salir' para terminar.\n>").upper())
                    if solicitud.consecutivo=="SALIR":          #String que saca al usuario del bucle
                        quit()
                else:                                           #Condicional que llena el objeto de clase solicitud con los datos de la solicitud ingresada por el usuario
                        s=list(dic_pendientes.get(solicitud.consecutivo))
                        solicitud.fecha_input(s[0])
                        solicitud.solicitante_input(s[1])
                        solicitud.estado_input(s[2][0:8])
                        solicitud.a_quien_input(s[2][9:len(s[2])])
                        solicitud.cantidad_input(s[3])
                        solicitud.criptomoneda_input(s[4])
            if responder=="Y":                                  #Cuándo el usuario decide responder una solicitud de transferencia hecha por otro usuario
                saldo_usd=usuario.registro.get("USD")                
                if not usuario.registro.get(solicitud.criptomoneda):    #Revisa si el usuario tiene en su saldo la criptomoneda solicitada
                    saldo_cripto=0                                      #Si no tiene la criptomoneda solictada pone un 0 en el saldo para evitar errores tipo NonType en condicionales más adelante en éste código
                else:
                    saldo_cripto=usuario.registro.get(solicitud.criptomoneda)   #Si tiene la criptomoneda solicitada la guarda en la variable saldo_cripto
                if not usuario.registro.get(solicitud.criptomoneda) or int(solicitud.cantidad)>saldo_cripto:    #Condicional que verifica si el saldo del usuario es suficiente para hacer la transferencia solicitada
                    valor_cripto=float(consultar_cryptos().get(solicitud.criptomoneda)[1])  #Variable que guarda el valor en USD registrado en coinmarketcap de la criptomoneda solicitada
                    responder=input("\n\nUsted no tiene saldo suficiente en " + solicitud.criptomoneda + "\nDesea adquir " + solicitud.criptomoneda + "?\n(Cada " + solicitud.criptomoneda + " se cotiza en USD$ " + str(valor_cripto) + ")\nY/N>").upper()
                    if responder=="Y":
                        comprar_criptos(usuario.code, saldo_usd, solicitud.criptomoneda)    #Llamado a la función que permite comprar la criptomoneda solictada
                    else:
                        print("Transacción terminada")                                      #Si decide cancelar la compra sale del programa
                        quit()
                else:                                                   #Cuándo el usuario tiene saldo suficiente en la criptomoneda solicitada
                    valor_cripto=float(consultar_cryptos().get(solicitud.criptomoneda)[1])  #Variable que guarda el valor en USD registrado en coinmarketcap de la criptomoneda solicitada
                    transfiere_criptos(solicitud.criptomoneda, solicitud.cantidad, usuario.code, solicitud.solicitante, valor_cripto)   #Función que gestiona la transferencia solicitada
                    usuario.registro_input(file_to_dic(str(os.getcwd() + "/files/usersfile.txt"),"*"))  #Extrae los datos de saldo almacenados en el archivo /files/usersfile.txt del usuario
                    usuario.registro_input(traduce_reg_a_dic(usuario.registro.get(usuario.code)[2]))    #Convierte en diccionario los saldos del usuario para su fácil manipulación
                    print("Criptomoneda solicitada:\t" + solicitud.criptomoneda)
                    print("Cantidad solicitada:\t\t" + solicitud.cantidad)
                    print("Se ha hecho la transferencia a " + solicitud.solicitante[0:len(solicitud.solicitante)-4])
                    print("Su saldo es:")
                    for saldo in usuario.registro:
                        print(saldo + ":\t" + '{:,.2f}'.format(usuario.registro.get(saldo)))
                    dic_pendientes.pop(solicitud.consecutivo)           #Borra del listado la solicitud que ya se gestionó
                    
                    directorio= str(os.getcwd() + "/files/solicitudes.txt") #Extrae la ruta del archivo /files/usersfile.txt para usarla en la siguiente función
                    reescribe(directorio, dic_pendientes)               #Actualiza los saldos en el archivo /files/usersfile.txt
                    
                    directorio= str(os.getcwd() + "/files/extracto_")   #Extrae la ruta del archivo donde se almacenan los movimientos del usuario para usarla en la siguiente función
                    archivo = open(str(directorio + usuario.user + usuario.code + ".txt") , "a")    #Abre el archivo de extractos del usuario
                    fecha= date_translate()
                    consecutivo= get_consec(archivo.name)               #Función para obtener el número consecutivo que sigue en el archivo del usuario
                    archivo.write("\n" + consecutivo + "*" + fecha + "*transferencia aprobada a " + solicitud.solicitante + "*" + solicitud.cantidad + "*" + solicitud.criptomoneda + "*" + str(valor_cripto)) #String que se registrará en el archivo del usuario que transfiere
                    archivo.close()
                    archivo = open(str(directorio + solicitud.solicitante+ ".txt") , "a")   #Extrae la ruta del archivo donde se notificará al usuario receptor de la transferencia
                    consecutivo= get_consec(archivo.name)               #Función para obtener el número consecutivo que sigue en el archivo del usuario receptor
                    archivo.write("\n" + consecutivo + "*" + fecha + "*deposito aprobado por " + usuario.user + usuario.code + "*" + solicitud.cantidad + "*" + solicitud.criptomoneda)  #String que se registrará en el archivo del usuario que recibe la transferencia
                    archivo.close()

            elif responder=="N":                                        #Cuándo la respuesta a la solicitud de transferencia es "Rechazar"
                rechazar_transferencia(dic_pendientes, solicitud, usuario.code)    #Función que actualiza los archivos de /files/solicitudes.txt, extracto del usuario solicitante, extracto del usuario al que se le hizo la solicitud
    else:
        responder=input("Desea hacer una nueva transferencia?\nY/N>").upper()   #Condicional que permite al usuario iniciar una transferencia sin que haya una solicitud de otro usuario
        if responder=="Y":
            participantes=file_to_dic(str(os.getcwd() + "/files/usersfile.txt"), "*")   #Variable donde se almancenan todos los usuarios registrados en la aplicación
            os.system("cls")
            print("Estos son los usuarios a los que puede transferir criptomonedas:")
            for p in participantes.keys():                              #Bucle que excluye del listado de participantes al usuario
                if p == "":
                    continue
                if p == usuario.code:
                    continue
                print(p + "\t" + participantes.get(p)[0])
            solicitud.solicitante_input(input("Ingrese el código del usuario a quien le hara la transferencia:\n>"))
            os.system("cls")
            criptos_disponibles=consultar_cryptos()                     #Variable que guarda las criptomonedas disponibles en coinmarketcap.com
            print("Estas son las criptomonedas disponibles:")
            print(list(criptos_disponibles.keys()))                     #Se muestran solo los nombres de las criptomonedas disponibles en coinmarketcap.com
            solicitud.criptomoneda_input(input("\nQué criptomoneda desea transferir?\n"))
            while not criptos_disponibles.get(solicitud.criptomoneda):  #Bucle que valida que el usuario digite correctamente el nombre de la criptomoneda a trasferir
                solicitud.criptomoneda_input(input("La criptomoneda señalada no está en la lista\nIntente de nuevo por favor\n>"))
            print("Cada " + solicitud.criptomoneda + " se cotiza en USD$ " + str(list(criptos_disponibles.get(solicitud.criptomoneda))[1])) #Imprime el valor cotizado de la criptomoneda que va a trasferir
            solicitud.cantidad_input(input("Cuántas criptomonedas desea transferir?\n>"))
            reg_saldos= traduce_reg_a_dic(usuario.registro)             #Importa en forma de diccionario los saldos del usuario para hacerlos manipulables por la función
            saldo_usd=int(reg_saldos.get("USD"))                        #Extrae el saldo de USD que tiene el usuario
            valor_cripto=criptos_disponibles.get(solicitud.criptomoneda)[1] #Guarda el valor en USD de la criptomoneda solicitada
            if not reg_saldos.get(solicitud.criptomoneda):              #Si el usuario no posee la criptomoneda en su saldo, agrega la criptomoneda en el diccionario de saldos y le da un saldo de 0
                reg_saldos[solicitud.criptomoneda]=0
            if float(solicitud.cantidad) > float(reg_saldos.get(solicitud.criptomoneda)):   #Condicional que evalúa si el saldo en criptomonedas es suficiente para hacer la trasferencia 
                comprar_criptos(usuario.code, saldo_usd, solicitud.criptomoneda)            #Si no es suficiente llama a la función de comprar criptomonedas para aumentar el saldo de la criptomoneda que va a transferir
                transfiere_criptos(solicitud.criptomoneda, solicitud.cantidad, usuario.code, solicitud.solicitante, valor_cripto)   #Luego de tener suficiente saldo en la criptomoneda hace el llamado a la función de transferir para continuar la transferencia
            else:
                transfiere_criptos(solicitud.criptomoneda, solicitud.cantidad, usuario.code, solicitud.solicitante, valor_cripto)   #Luego de tener suficiente saldo en la criptomoneda hace el llamado a la función de transferir para continuar la transferencia
        else:
            print("Transferencia rechazada")                            #En caso de que se decida rechazar la solicitud de transferencia
