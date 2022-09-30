#Es el módulo donde se recopila toda la información de los diferentes DocString de los módulos que usa la aplicación para mostrarlos de una manera ordenada a través de la consola.
import inspect
import os
from proyecto_final import main_menu

menu=[]
me=""
for file in os.listdir():                                       #mostrar en pantalla la descripción consignada en cada función a través del método DocString
        if file.endswith(".py"):
            menu.append(file)
menu.insert(0,"")         

print("En esta opción podrá encontrar la documentación del proyecto organizado de la siguiente manera:\n")

def documentar():
    """
    Función que genera un menú a través del listado de modulos en el proyecto. con la función listdir() que se encuentra en el módulo \"os\"
    Trae con el módulo \"inspect \" usando la función \"getmodulename\" las funciones \"isfunction\" que hacen parte de cada módulo del proyecto y muestra por pantalla el DocString o ayuda de la función.
    """
    for m in range(len(menu)-1):
        if m ==0:
            continue                                    #Imprime el menú de módulos
        print(str(m) + "\t" + menu[m])

    print("\nDigite el número de la opción que quiere visualizar:") #Valida que el usuario ingrese una opción correcta del menú
    try:
        seleccion=int(input(">"))
    except:
        seleccion=input(">")
    while not isinstance(seleccion, int):                           #Si no es un número detecta el error 
        try:
            if seleccion=="SALIR":
                quit()
            seleccion=int(input("Opción invalida, por favor intente de nuevo o digite \"SALIR\"\n>"))
        except:
            if seleccion=="SALIR":
                quit()
            seleccion=input("Opción invalida, por favor intente de nuevo o digite \"SALIR\"\n>")
            
    while seleccion > len(menu) or seleccion <1:                    #Si el usuario digita una opción fuera del rango del menú detecta el erro
        try:
            if seleccion=="SALIR":
                quit()
            seleccion=int(input("Opción invalida, por favor intente de nuevo o digite \"SALIR\"\n>"))
        except:
            if seleccion=="SALIR":
                quit()
            seleccion=input("Opción invalida, por favor intente de nuevo o digite \"SALIR\"\n>")

    if seleccion>=0 or seleccion<=len(menu):
        print("El modulo " + str(menu[seleccion]).upper() + " está compuesto por las siguientes funciones:")
        me = __import__(inspect.getmodulename(menu[seleccion]))
        help(me)
            
documentar()    