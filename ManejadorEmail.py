from Email import Email
import csv

class ManejadorEmail:
    __listaEmail= []

    def __init__(self):
        self.__listaEmail= []

    def agregadorEmail(self, mail):
        self.__listaEmail.append(mail)

    def contadorDominio(self):
        print("Dominios Repetidos")
        domi= input("Ingrese dominio:  ")
        c=0
        for Email in self.__listaEmail:
            if Email.getDominio() == domi:
                c+=1
        if c == 0:
            print("No existe ningún Email, con el dominio ingresado")
        else:
            print("Existen {} Email/s con el dominio ingresado \n" .format(c))


    def manejadorArchi(self):
        archivo= open('correos.csv')
        reader= csv.reader(archivo,delimiter=';')
        objetoemail= Email()
        for fila in reader:
            emailnuevo= objetoemail.crearCuenta(fila[0])
            self.agregadorEmail(emailnuevo)
        self.contadorDominio()
