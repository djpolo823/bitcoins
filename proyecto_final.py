"""************************************************************************************************************
Billetera digital tipo desktop con la que se puede: 
    1. envía y recibe un monto en USD de las criptomonedas registradas en coinmarketcap
    2. Consulta el balance de cada criptomoneda de la que el usuario posee
    3. Consulta el balance en USD usando el precio de cada criptomoneda registrada en coinmarketcap
    4. Emite histórico de transacciones con fecha, moneda, cantidad y monto en USD
    5. Almacena las transacciones y las cantidades de cada criptomoneda que el usuario posee

MENÚ:

    1 Recibir cantidad:
        Solicitar moneda, cantidad a recibir, así como el código.
        Validar moneda, cantidad y código, éste debe ser diferente al propio.
        Sumar cantidad de monedas al saldo.
    2 Transferir monto:
        Solicitar moneda, monto y código del destinatario a enviar.
        Validar.
        Restar cantidad de monedas al saldo.
    3 Mostrar balance de una moneda:
        Solicitar la moneda a mostrar
        Validar existencia de la moneda.
        Mostrar nombre de la moneda, cantidad y monto en USD para ese momento.
    4 Mostrar balance general:
        Mostrar nombre de cada moneda, cantidad y monto en USD para ese momento.
        Mostrar monto total en USD de todas las monedas.
    5 Mostrar histórico de transacciones:
        Mostrar todas las transacciones indicando fecha, moneda, tipo de operación, código del usuario, cantidad y monto para el momento.
    6 Salir del programa

API de consulta https://pro-api.coinmarketcap.com

************************************************************************************************************"""
#IMPORTANDO MODULOS NECESARIO
import os
from balance_de_moneda import consulta_cripto_individual
from balance_general import consulta_registro_saldo
from extracto import mostrar_extracto
from login import usuario, valida_usuario
from recibe import recibir
from transferir import transferencia
from funciones.file_to_dic import *

#INGRESO DEL USUARIO A LA APLICACIÓN**************************************************************************

os.system("cls")                                                            #limpia la pantalla para el menú

print("Para efectos de la evaluación de los tutores de NEXTU, aquí se mostrarán los usuarios con sus respectivos datos de ingreso:\n\n")

todos= file_to_dic(str(os.getcwd() + "/files/usersfile.txt"),"*")

print("Código/nombre/contraseña\n" )
for u in todos:
    print(u + " " + todos.get(u)[0] + " " + todos.get(u)[1])

valida_usuario()

print("\nElija entre una de las siguientes opciones:")
#MENÚ INICIAL*******************************************************************************************************
menu= ["1 Recibir cantidad","2 Transferir monto","3 Mostrar balance de una moneda","4 Mostrar balance general","5 Mostrar historico de transacciones","6 Salir", "7 Documentación del proyecto"]

for x in range(len(menu)):
    print(menu[x])

opcion=int(input("Qué opción desea elejir?\n>"))

os.system("cls")

print("Usted eligió la opción número: " + menu[opcion-1] + "\n")
#FIN DEL MENÚ*******************************************************************************************************
if opcion == 1:
    recibir(usuario)
elif opcion == 2:
    transferencia(usuario)
elif opcion == 3:
    consulta_cripto_individual(usuario)
elif opcion == 4:
    consulta_registro_saldo(usuario, opcion)
elif opcion == 5:
    mostrar_extracto(usuario)
elif opcion == 6:
    print("Esperamos que vuelva pronto")
elif opcion == 7:
    os.system('documentacion.py')
else:
    print("Opción no valida")
