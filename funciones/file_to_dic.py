import os

def file_to_dic(file,character):
    """
    Función que separa un archivo en reglones y genera un diccionario con los datos de cada reglón.
    Argumento 1: String del path y nombre del archivo
    Argumento 2: Caractér que separa cada dato dentro del reglón para identificarlo como un dato
    """
    archivo=open(file,"+r")                     #Abre el archivo
    reglon=archivo.read().split("\n")           #Separa los reglones del archivo
    dic={}                                      #Crea un diccionario
    for line in range(len(reglon)):             #Bucle para separar cada reglón en datos individuales
        if reglon=="":
            continue
        register=reglon[line].split(character)  
        valores=[]                              #Crea una lista para ingresar los valores del diccionario
        for v in range(1,len(register)):        #Agrega los datos a la lista de valores
            valores.append(register[v])
        dic[register[0]]=valores                #Asigna clave y valores del diccionario
    archivo.close()
    return dic

def get_consec(archivo):
    """
    Función que separa un archivo en reglones para luego extraer los primeros 6 caracteres del reglón y convertirlos en un consecutivo, agregando en el return el consecutivo que sigue.
    """
    archivo_solicitudes=open(archivo,"r")               #Abre el archivo donde están los datos
    reglon=archivo_solicitudes.read().split("\n")       #Separa en reglones el archivo
    
    for ultimo in range(len(reglon)):                   #Busca el segmento inicial de 6 digitos donde debería estar el consecutivo del registro
        consecutivo=reglon[ultimo][0:6]
    if consecutivo=="":                                 #Cuando no hay un consecutivo asigna uno que vale 0
        consecutivo=0
    consecutivo=int(consecutivo)+1                      #Suma uno al último consecutivo que estaba en el archivo
    consecutivo='{:0>6}'.format(consecutivo)            #Le asigna un formato al consecutivo para que siempre tenga 6 dígitos
    archivo_solicitudes.close()
    return consecutivo