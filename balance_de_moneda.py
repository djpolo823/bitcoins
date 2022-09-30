from login import *
from modulos.criptomonedas import consultar_cryptos
from modulos.classes import Criptomoneda
from funciones.reg_to_dic import traduce_reg_a_dic

def consulta_cripto_individual(myself):
    """
    Función que consulta la base de datos de coinmarketcap.com y genera un informe de la moneda que el usuario ingrese en la entrada de datos
    Así mismo le dice al usuario si posee en su saldo la criptomoneda que está cotizando y le muestra su cotización actual en USD
    """
    todas_las_criptos= consultar_cryptos()              #Guardamos en un diccionario local el listado de todas las criptomonedas en la base de marketcoincap
    mis_criptos= traduce_reg_a_dic(usuario.registro)    #Guardamos en un diccionario local las criptomonedas que el usuario posee y sus saldos 
    criptomoneda = input("\nIngrese el nombre de la criptomoneda que desea consultar:\n>")
    if todas_las_criptos.get(criptomoneda):             #Validamos que la criptomoneda en la entrada de texto exista en el listado de coinmarketcap
        if mis_criptos.get(criptomoneda):               #Validamos que el usuario posea en su saldo la criptomoneda en la entrada de texto             
            moneda=  Criptomoneda(criptomoneda, int(mis_criptos.get(criptomoneda)), float(todas_las_criptos.get(criptomoneda)[1]))#Instanciamos la clase Criptomoneda con los valores de saldo del usuario
        else:
            moneda= Criptomoneda(criptomoneda, 0, float(todas_las_criptos.get(criptomoneda)))#Instanciamos la clase Criptomoneda con los valores de la criptomoneda en coinmarketcap
        if mis_criptos.get(criptomoneda):
            print("\nCada " , moneda.mostrarnombre() , " " , str(todas_las_criptos.get(criptomoneda)[0]) , " está cotizada en " , 'USD$ {:,.2f}'.format(moneda.mostrarcotizacion()))    #Se muestra el valor en USD de cada criptomoneda
            print("Usted tiene un total de " , moneda.mostrarsaldo() , " " , moneda.mostrarnombre() , " que equivalen a " , 'USD$ {:,.2f}'.format(float(moneda.calcularsaldo(criptomoneda)))) #Se muestra el saldo en criptomonedas y su valor en USD
        else:
            print("Usted no tiene ninguna " , moneda.mostrarnombre() , "en su haber")
            print("\nCada " , moneda.mostrarnombre() , " " , str(todas_las_criptos.get(criptomoneda)[0]) , " está cotizada en " , 'USD$ {:,.2f}'.format(moneda.mostrarcotizacion())) 
    else:
        print("Esa moneda no registra en la base de datos")
        consulta_cripto_individual(myself)              #Cuándo el usuario ingresa un nombre de criptomoneda que no existe, el programa regresa al inicio de la función