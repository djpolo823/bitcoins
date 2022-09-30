import os
from login import *
from funciones.date_translate import date_translate

def calcula_tabulaciones(diccionario):
    """
    Función que mide el largo de cada dato y calcula el espacio correcto en una columna para que los datos se vean de manera organizada.

    Como argumento recibe los datos de las transacciones realizadas por el usuario, los organiza en fecha, detalle del movimiento, monto, moneda y cotización.  Buscando para cada columna cúal es el string más largo de esa columna y asignando el tamaño de la columna de acuerdo al string más largo.
    """
    largo_dato=[0,0,0,0,0]                              #Lista donde se almacenará el valor más alto de la longitud de los datos que contiene cada columna
    n=0
    titulos=["FECHA\t\t\t\t\t", "DETALLE", "MONTO", "MONEDA", "COTIZACIÓN EN USD$"] #Listado de los titulos de cada columna, necesario para calcular el espacio que necesitan en el documento
    for registro in diccionario.keys():                 #Bucle que recorre todo el diccionario y guarda en el listado de longitud de columna el valor más alto de longitud de los strings
        for ancho in range(5):            
            if largo_dato[ancho]<len(list(diccionario.get(registro))[ancho])-1:
                print(list(diccionario.get(registro))[ancho])
                largo_dato[ancho]=len(list(diccionario.get(registro))[ancho])-1

    for registro in diccionario.keys():                 #Bucle que asigna a cada string la cantidad de espacios en blanco que necesita para salir bien tabulado en el informe
        if registro=="":
            continue
        for dato in range(5):
            if dato==0:
                diccionario.get(registro)[dato]="".join(diccionario.get(registro)[dato].rjust(largo_dato[dato]+5))  #Se trae el string, se consulta cuál es el string más largo de esa columna y se le suman espacios en blanco al string hasta llegar a la longitud máxima en la columna donde se encuentra el string
            else:
                diccionario.get(registro)[dato]="".join(diccionario.get(registro)[dato].ljust(largo_dato[dato]+5))  #Se trae el string de titulo, se consulta cuál es el string más largo de esa columna y se le suman espacios en blanco al string de titulo hasta llegar a la longitud máxima en la columna donde se encuentra el string
                titulos[dato]="".join(titulos[dato].ljust(largo_dato[dato]+6))

        reglon=list(diccionario.get(registro))          #Se guarda en una lista los strings generados en el bucle anterior para imprimirlos en el informe de manera organizada y tabulada
        if n==0:
            print("DOC.  \t\t" + titulos[0] + titulos[1] + titulos[2] + titulos[3] + titulos[4] + "\t\t\n") #Imprime el titulo solo en el primer reglon del bucle
            n = n+1
        print(str(registro) + "\t" + reglon[0] + "\t" + reglon[1] + reglon[2] + reglon[3] + reglon[4])  #Imprime en orden cada reglon del informe

def mostrar_extracto(myself):
    """
    Función que muestra de manera organizada el informe de movimientos que ha hecho el usuario desde la apertura de la cuenta.
    """

    fecha = date_translate()

    print("Informe de movimientos\t\t\t" + fecha)           #Imprime el membrete del documento
    print("Usuario:\t\t" + usuario.user)            
    print("Código de usuario:\t" + usuario.code + "\n\n")

    datos= file_to_dic(str(os.getcwd() + "/files/extracto_" + usuario.user + usuario.code + ".txt"), "*")   #Crea un diccionario con los datos del extracto del usuario
    calcula_tabulaciones(datos)                             #Envía el diccionario generado a la función calcula_tabulacionespara organizar la información en columnas