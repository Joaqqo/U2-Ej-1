from Email import Email
from ManejadorEmail import ManejadorEmail

if __name__ == "__main__":
    nombre= input("Ingrese su nombre:  ")
    dominio= input("Ingrese el dominio de su cuenta:  ")
    tipoDom= input("Ingrese el tipo de dominio de su cuenta:  ")
    correo= input("Ingrese su usuario de correo:  ")
    password= input("Ingrese su contraseña:  ")

    email= Email(correo, dominio, tipoDom, password)

    print("Estimado {} te enviaremos tus mensajes a la dirección {} ".format(nombre, email.__str__()))
#---------------------------------------------------------------
    print("--CAMBIO DE CONTRASEÑA--")
    contraseniaActual= input("Ingrese su contraseña actual: ")
    email.cambiaContra(contraseniaActual)
#---------------------------------------------------------------

    nuevoEmail= input("Ingrese un Email nuevo:  ")
    objEmailnuevo= Email()
    EmailNuevo= objEmailnuevo.crearCuenta(nuevoEmail)

    objEmailnuevv= ManejadorEmail()
    objEmailnuevv.manejadorArchi()


