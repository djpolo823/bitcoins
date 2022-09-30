from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, code, user, password, registro):
        self.code= code
        self.user= user
        self.password= password
        self.registro= registro
    
    @abstractmethod
    def code_input(self):
        pass
    def user_input(self):
        pass
    def password_input(self):
        pass
    def registro_input(self):
        pass

class class_cripto_user(Usuario):
    def __init__(self, code, user, password, registro):
        super().__init__(code, user, password, registro)
        self.code= code
        self.user= user
        self.password= password
        self.registro= registro
    def code_input(self, code):
        self.code= code
    def user_input(self, user):
        self.user= user
    def password_input(self, password):
        self.password= password
    def registro_input(self, registro):
        self.registro= registro
    def imprime(self):
        print("usuario: ", self.user, "\ncode: ", self.code, "\npassword: " , self.password, "\nregistro:\n", self.registro)

class Criptomoneda(object):
    def __init__(self, nombre, saldo, cotizacion):
        self.nombre = nombre
        self.saldo = saldo
        self.cotizacion = cotizacion
    
    def indicarnombre(self, nombre):
        self.nombre= nombre

    def indicarcotizacion(self, cotizacion):
        self.cotizacion = cotizacion

    def indicarsaldo(self, saldo):
        self.saldo = saldo
    
    def mostrarnombre(self):
        return self.nombre

    def mostrarcotizacion(self):
        return self.cotizacion

    def mostrarsaldo(self):
        return self.saldo


    def calcularsaldo(self, moneda):
        #if moneda=="USD":
        return self.saldo*self.cotizacion
        #else:
        #    return self.saldo           

class Solicitud(object):
    def __init__(self, a_quien, consecutivo, fecha, solicitante, estado,  cantidad, criptomoneda):
        self.a_quien=a_quien
        self.cantidad=cantidad
        self.consecutivo=consecutivo
        self.criptomoneda=criptomoneda
        self.estado=estado
        self.fecha=fecha
        self.solicitante=solicitante

    def consecutivo_input(self, consecutivo):
        self.consecutivo=consecutivo
    def fecha_input(self, fecha):
        self.fecha= fecha
    def solicitante_input(self, solicitante):
        self.solicitante= solicitante
    def estado_input(self, estado):
        self.estado= estado
    def a_quien_input(self, a_quien):
        self.a_quien= a_quien
    def cantidad_input(self, cantidad):
        self.cantidad= cantidad
    def criptomoneda_input(self, criptomoneda):
        self.criptomoneda= criptomoneda