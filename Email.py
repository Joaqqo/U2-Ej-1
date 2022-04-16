import re

class Email:
    __idCuenta= ""
    __dominio= ""
    __tipoDominio= ""
    __contra= ""

    def __init__(self, idC= "", dom="", tipoDom="", contras=""):
        self.__idCuenta= idC
        self.__dominio= dom
        self.__tipoDominio= tipoDom
        self.__contra= contras

    def __str__(self): #Aca sería el retornaEmail()
        return '{}@{}.{}' .format(self.__idCuenta, self.__dominio, self.__tipoDominio)

    def getDominio(self):
        return self.__dominio

    def cambiaContra(self, contrasenia):
        if self.__contra == contrasenia:
            print("Contraseña Correcta")
            nuevaContra= input("Por favor ingrese su nueva contraseña:  ")
            self.__contra= nuevaContra
        else:
            print("Contraseña Incorrecta")

    def crearCuenta(self, mail):
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', mail.lower()): #Comprueba que el formato de mail esté bien
            print("Verificado el correo, está de forma correcta. \n")
            ma, ma1= mail.split("@")
            ma1, ma2= ma1.split(".")
            #usuario@hotmail.com --> ma=usuario | ma1=hotmail | ma2=com
            contrass= input("Ingrese contraseña para su mail {}:  " .format(ma))
            emailnuevo= Email(ma, ma1, ma2, contrass)
            print("¡Su email fue creado exitosamente! \n")
            return emailnuevo
        else:
            print("\n El correo ingresado no está en su forma correcta. \n")
