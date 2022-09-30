from funciones.actualiza_archivos import movimiento_cliente, reescribe
from funciones.file_to_dic import file_to_dic, get_consec
from funciones.reg_to_dic import traduce_reg_a_dic
from funciones.date_translate import date_translate
import os
from modulos.criptomonedas import consultar_cryptos
from login import usuario

def comprar_criptos(usuario, saldo, cripto):
    directorio=str(os.getcwd() + "/files/")
    dic_saldo_usuarios=file_to_dic(str(directorio + "usersfile.txt") , "*")

    valor_cripto=float(consultar_cryptos().get(cripto)[1])
    saldo_usd=saldo
    if valor_cripto<=saldo_usd:
        cantidad_criptos=saldo_usd//valor_cripto
        comprar=int(input("Puede comprar " + str(cantidad_criptos) + " " + cripto + ".\n¿Cuántos " + cripto + " desea comprar?>"))
        if comprar<= cantidad_criptos:
            saldo_usd=saldo_usd - (valor_cripto*comprar)
            saldo=traduce_reg_a_dic(dic_saldo_usuarios.get(usuario)[2])
            saldo["USD"]=saldo_usd
            saldo[cripto]=comprar
            datos_usuario=list(dic_saldo_usuarios.get(usuario))
            datos_usuario[2]=saldo
            dic_saldo_usuarios[usuario]=datos_usuario
        else:
            print("Su saldo no es suficiente para comprar esa cantidad de " + cripto)
            comprar_criptos(usuario, saldo, cripto)
    
        open(str(directorio +"usersfile.txt"), "w").close()
        archivo= open(str(directorio + "usersfile.txt"), "a")

        contador = len(list(dic_saldo_usuarios.keys()))
        for k in list(dic_saldo_usuarios.keys()):
            escribe=""
            contador= contador-1
            for i in list(dic_saldo_usuarios.get(k)):
                escribe=str(escribe) + "*" + str(i)
            escribe= k + escribe
            if contador!=0:
                escribe=escribe + "\n"
            archivo.write(escribe)
        archivo.close()

        archivo=open(str(directorio + "extracto_" + datos_usuario[0] + usuario + ".txt") , "a")
        fecha= date_translate()      
        consecutivo = get_consec(archivo.name)  
        archivo.write("\n" + consecutivo + "*" + fecha + "*Compra_de_criptomoneda*" + str(comprar) + "*" + cripto + "*USD$" + str(valor_cripto*comprar))
        archivo.close()

    else:
        print("Su saldo no es suficiente para comprar " + cripto)
        quit()
    print("Saldo general:\t")
    
    for s in saldo.keys():
        if s == "USD$":
            continue
        print("Saldo en " + s + ":\t" + str(saldo[s]))    

def transfiere_criptos(cripto, cantidad, registro, solicita, valor):
    directorio = str(os.getcwd() + "/files/")
    archivo = open(str(directorio + "usersfile.txt"), "a")
    dic_usuarios=file_to_dic(str(directorio + "usersfile.txt"), "*") #Diccionario con todos los usuarios
    
    #Emisor
    datos_usuario=list(dic_usuarios.get(registro)) #Datos de quien hará la transferencia
    saldo_usuario=datos_usuario[2]  #Saldo de quien hará la transferencia
    saldo_cripto=traduce_reg_a_dic(saldo_usuario) #Diccionario de saldos de quien transfiere
    saldo_cripto[cripto]=float(saldo_cripto.get(cripto)) - float(cantidad) #Resta de la cantidad transferida al saldo de quien transfiere
    datos_usuario[2]=saldo_cripto   #Se almacena el cambio en el diccionario de datos de quien transfiere
    dic_usuarios[registro]=datos_usuario

    #Receptor
    solicita= solicita[len(solicita)-4:len(solicita)]
    datos_usuario=list(dic_usuarios.get(solicita))  #Datos de quien recibe la transferencia
    saldo_usuario=datos_usuario[2]  #Saldo de quien recibe la transferencia
    saldo_cripto=traduce_reg_a_dic(saldo_usuario)   #Diccionario de saldos de quien recibe
    saldo_cripto[cripto]=float(cantidad)  #Suma de la cantidad transferida al saldo de quien recibe
    datos_usuario[2]=saldo_cripto   #Se almacena el cambio en el diccionario de datos de quien recibe
    dic_usuarios[solicita]=datos_usuario    #Se almacena el cambio en el diccionario de datos de quien transfiere

    open(str(directorio + "usersfile.txt"), "w").close()
    archivo=str(directorio + "usersfile.txt")
    reescribe(archivo,dic_usuarios)

    nombre_archivo=str(usuario.user + usuario.code)
    movimiento=["transferencia a", datos_usuario[0], solicita, cantidad,cripto, valor]
    movimiento_cliente(nombre_archivo, movimiento)

    nombre_archivo=str(datos_usuario[0] + solicita)
    movimiento=["transferencia de", usuario.user, usuario.code, cantidad,cripto, valor]
    movimiento_cliente(nombre_archivo, movimiento)