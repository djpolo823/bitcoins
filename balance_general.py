#Abrir y consultar el registro del usuario que hace la transacción
#Mostrar nombre de cada moneda, cantidad y monto en USD para ese momento.

from funciones.reg_to_dic import traduce_reg_a_dic
import os
from login import *
from modulos.criptomonedas import consultar_cryptos
from modulos.classes import Criptomoneda

def consulta_registro_saldo(myself, opcion):
    """Función que consulta y presenta en un informe el saldo que posee en usuario en USD y en criptomonedas,"""
    """además de consultar el valor actual de cada criptomoneda del saldo en la aplicación coinmarketcap.com """
    """totalizando en USD el slado del usuario."""
        
    saldo=0                                             #Crea variable para manejar saldos y la inicializa en 0
    myself=usuario.code                                 #Trae el código del usuario para hacer las consultas 
    archivo= str( os.getcwd() + "/files/usersfile.txt") #Abre el archivo /files/usersfile.txt para extrael los datos de saldo del usuario
    cripto=file_to_dic(archivo, "*")
    cripto=traduce_reg_a_dic(cripto.get(myself)[2])
    dic_saldo_criptos={}                                #Crea in diccionario para poder manejar la información de saldos
    dic_todas_las_criptos=consultar_cryptos()           #Crea un diccionario para manejar los datos de todas las criptomonedas mostradas en coinmarketcap.com
    
    for k in cripto:

        if k == "USD":                                  #Agrega al diccionario el saldo en USD del usuario
            print(k)
            print("\tSaldo:\t\t\t" 'USD$ {:,.2f}'.format(cripto.get(k)))
            saldo=saldo+cripto.get(k)
            continue
        else:                                           #Agrega al diccionario las criptomonedas que el usuario tiene en su saldo
            mis_criptos=Criptomoneda(k,float(cripto.get(k)),float(dic_todas_las_criptos.get(k)[1]))
            dic_saldo_criptos[mis_criptos.nombre]=mis_criptos.saldo
            
            if opcion==4:                               #Imprime en pantalla los datos detallados del saldo 
                print("\n" + mis_criptos.mostrarnombre())
                print("\tCantidad:\t\t" , mis_criptos.mostrarsaldo(), "unidades")
                print("\tCotización actual:\t" 'USD$ {:,.2f}'.format(mis_criptos.mostrarcotizacion()))
                print("\tSaldo:\t\t\t" 'USD$ {:,.2f}'.format(mis_criptos.calcularsaldo(k)))
            saldo=saldo+mis_criptos.calcularsaldo(k)
    if opcion==4:
        print("\nUsted tiene en total " + 'USD$ {:,.2f}'.format(saldo))