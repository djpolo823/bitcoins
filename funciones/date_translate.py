from datetime import datetime
dias=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
mes=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
months=["January","February","March","April","May","June","July","August","September","October","November","December"]
def date_translate():
    """
        Función que recibe un argumento tipo \"date\", toma los datos del día de la semana y el mes, los busca en un listado y con el indice del elemento hace una busqueda dentro e otra lista donde se encuentran los días y meses en español y hace un reemplazo con los datos en español dentro de otra lista.
    """
    fecha=datetime.today().strftime("%A %d de %B de %Y %I:%M:%S %p")    #Fecha actual con el formato día de la semana, día del mes, mes, año y hora formato de 12 horas
    separa=fecha.split(" ")                                             #Separa los elementos del string fecha
    separa[0]=dias[days.index(separa[0])]                               #Toma el inice del día en ingles y lo reemplaza con el índice del día en español
    separa[3]=mes[months.index(separa[3])]                              #Toma el inice del mes en ingles y lo reemplaza con el índice del mes en español
    espacio=" "
    fecha_esp=espacio.join(separa)                                      #Reagrupa los elementos de la lista fecha en un string separado por el caractér de espacio " "
    return fecha_esp

date_translate()