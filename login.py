#Login es el módulo donde se registran los usuarios, se validan los datos de nombre, código y contraseña de usuario.  Es la primera pantalla que verán los usuarios al usar la aplicación.

from funciones.actualiza_archivos import reescribe
from funciones.date_translate import date_translate
from os import system
from modulos.classes import class_cripto_user
import getpass, random
from funciones.file_to_dic import file_to_dic


saldo={}#Diccionario para guardar los saldos de las diferentes criptomonedas del usuario
usuario=class_cripto_user("","","",saldo)#Clase usuario, guarda información del login

def valida_usuario():   
    """Función desde donde se abrirá el archivo de usuarios /files/usersfile.txt crea un diccionario dic_user de manera global con los datos del usuario que está haciendo login, con el cuál se hará la validación de los datos de usuario para poder acceder a la aplicación"""
    global count
    count = 0
    global dic_user                                 #Diccionario como variable global para validar la información del login contra el archivo donde se guardan los datos de los usuarios
    dic_user=file_to_dic("files/usersfile.txt","*") #Función que convierte un archivo de texto en un diccionario
    valida_code()                                   #Llamado a función para validar el código ingresado por el usuario
    return usuario

def registra_usuario(): 
    """Función que habilita al usuario para crear una cuenta nueva agregando un nombre de usuario, una contraseña y un saldo en USD$ dolares para comenzar a usar la aplicación.\n\n    
    Para almacenar los datos del usuario se creó una clase usuario, donde se almacenan los datos \n
    NOMBRE: a través de usuario.user
    CÓDIGO: usuario.code; que lo genera el sistema automáticamente de manera aleatoria y teniendo en cuenta que no coincida con el código de otro usuario. 
    CONTRASEÑA: usuario.password que utiliza la librería getpass para evitar que la contraseña sea visible para otras personas al momento de digitarla.
    SALDO EN USD: Podrá abrir la cuenta con un monto en dolares que el usuario elija.  Este saldo se almacenara en el archivo de usuarios para ser consultado en cualquier parte de la aplicación y disponer del saldo para comprar criptomonedas.

    La validación de la contraseña consiste en evaluar que la contraseña no contenga menos de 4 digitos y se le pide al usuario confirmar por segunda vez la contraseña que ha creado.

    Al momento de crear el usuario, la aplicación generará un archivo de texto con el nombre y código del usuario donde se almacenarán  todas las transacciones del usuario para su posterior consulta.
    """

    system("cls")
    fecha=date_translate()                          #Función que traduce al español la fecha del sistema
    usuario.user_input(input("Por favor, ingrese el nombre de usuario que quiere registrar:\n>"))
    confirma_password=""
    while len(usuario.password)<4:                  #Valida que la contraseña ingresada no tenga menos de 4 digitos
        usuario.password_input(getpass.getpass("Ingrese un password que contenga más de 3 dígitos:\n>"))
    while confirma_password != usuario.password:    #Valida que la contraseña se haya escrito correctamente
        confirma_password=getpass.getpass("Por favor confirme el password que usará en la aplicación:\n>")
    usuario.code_input('{:0>4}'.format(random.randint(0,9999))) #Formatea el número a un string de 4 dígitos llenando los strings de menos de 4 dígitos con "0" a la izquierda
    while dic_user.get(usuario.code):
        usuario.code_input('{:0>4}'.format(random.randint(0,9999))) #Si el código asignado por el sistema ya lo tiene otro usuario, el sistema asigna otro nuevamente
    saldo["USD"]=int(input("Con qué monto en USD desea abrir su cuenta?:\n>"))
    usuario.registro_input(saldo)
    dic_user[usuario.code]=usuario.user,usuario.password,usuario.registro   #Agrega los datos de la clase usuario en el diccionario para reescribir el archivo de usuarios
    reescribe("files/usersfile.txt", dic_user)      #Función para reescribir el archivo usersfile.txt con el nuevo registro
    archivo=open(("files/extracto_" + usuario.user + usuario.code+ ".txt"),"a") #Crea un archivo para registrar las transacciones del usuario
    archivo.write("000001*" + fecha + "*apertura de cuenta* * * * \n000002*" + fecha + "*Deposito " + usuario.user + "*" + str(saldo.get("USD")) + "*" + "USD* ") #Agrega al registro del usuario los datos de apertura de la cuenta y el saldo inicial
    print("Su código de usuario es " + str(usuario.code))
    archivo.close()
    
def valida_code():
    """Función para validar si el código ingresado por el usuario existe o si se debe crear un nuevo usuario."""
    print("Bienvenido a su billetera virtual!:\n")
    registra=input("Si desea registrar un usuario nuevo digite R y luego oprima ENTER, de lo contrario digite su código:\n>").upper() #Esta línea recibe el código de usuario si ya existe; si no existe direcciona el programa a la función de registrar nuevo usuario
    if registra == "R":
        registra_usuario()                          #Función para registrar un nuevo usuario
        valida_usuario()                            #Luego de registrar el nuevo usuario el programa vuelve para permitir hacer login con el nuevo usuario
    else:
        usuario.code_input(registra)
        while not dic_user.get(usuario.code):       #Si ingresa un código que no exite el sistema da la opción para registrar el usuario
            registra=input("El código ingresado no existe.  ¿Desea registrarse?\nY/N\n>").upper()
            if registra=="Y":
                registra_usuario()                  #Función para registrar un nuevo usuario
                valida_usuario()                    #Luego de registrar el nuevo usuario el programa vuelve para permitir hacer login con el nuevo usuario
            else:
                print("Código no existe.  Intentalo de nuevo")  #Si no se registra el código, el programa se cerrará
                quit()
        valida_nombre()

def valida_nombre():
    """Función que valida si el nombre de usuario ingresado coincide con el código de usuario registrado en el archivo de usuarios usersfile.txt.
        Si el nombre no correspone al código, el sistema regresará al principio para que el usuario verifique la información ingresada.
    """
    usuario.user_input(input("Ahora, ingrese su nombre de usuario:\n>"))
    if usuario.user != dic_user.get(usuario.code)[0]: #Si el nombre ingresado es diferente al nombre registrado en el diccionario
        print("El nombre de usuario no corresponde al codigo.  Por favor intentelo nuevamente.\n")
        valida_usuario()                            #Regresa a la función inicial
    print("Por último")
    valida_password()                               #Si coinciden los datos se direcciona a la función que verifica la contraseña

def valida_password():
    """Función que valida si la contraseña ingresada corresponde a la que está registrada en el archivo usersfile.txt"""
    while usuario.password != dic_user.get(usuario.code)[1]:    #Mientras que el password no coincida volverá a preguntar la contraseña
        usuario.password_input(getpass.getpass("Ingrese su contraseña:\n>"))    #el método getpass hace que los datos ingresados en este campo no sean visibles en el promt
        if usuario.password != dic_user.get(usuario.code)[1]:
            print("Contraseña incorrecta.  Por favor intentelo nuevamente.\n")
            global count                            #Contador que indica la cantidad de veces que se ingresa erradamente la contraseña
            count = count + 1
            if count>=3:                            #si la contraseña es incorrecta devuelve el programa al inicio de la validación de contraseña
                print("Tercer intento fallido, por favor confirme sus datos y vuelva a intentarlo.")
                quit()
            valida_password()
    usuario.registro_input(list(dic_user.get(usuario.code))[2]) #Carga los saldos al diccionario de usuario
    system("cls")