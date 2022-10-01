# bitcoins
It´s an Python app that allows users to buy, send, ask for cryptocurrencies, all the information about cryptocurrencies is retrived from coinmarket.com API

"""*************************************************** ************************************************** ***********
Desktop type digital wallet with which you can:
    1. send and receive an amount in USD of the cryptocurrencies registered in coinmarketcap
    2. Check the balance of each cryptocurrency that the user owns
    3. Check the balance in USD using the price of each cryptocurrency registered in coinmarketcap
    4. Issue transaction history with date, currency, amount and amount in USD
    5. Stores the transactions and amounts of each cryptocurrency that the user owns

MENU:

    1 Receive quantity:
        Request currency, amount to receive, as well as the code.
        Validate currency, amount and code, this must be different from your own.
        Add number of coins to balance.
    2 Transfer amount:
        Request currency, amount and code of the recipient to send.
        Validate.
        Subtract amount of coins to the balance.
    3 Show balance of a currency:
        Request the currency to display
        Validate currency existence.
        Show currency name, amount and amount in USD for that moment.
    4 Show balance sheet:
        Show name of each currency, amount and amount in USD for that moment.
        Show total amount in USD of all currencies.
    5 Show transaction history:
        Show all transactions indicating date, currency, type of operation, user code, amount and amount for the moment.
    6 Exit program

Query API https://pro-api.coinmarketcap.com

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
