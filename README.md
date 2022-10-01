# bitcoins
It´s an Python app that allows users to buy, send, ask for virtual coins, all the information about virtual coins is retrived from coinmarket.com API

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
