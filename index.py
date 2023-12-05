import functions
import consultas

dec = input('''
            Qué desea hacer?
            
            1 - Agregar un contacto.
            2 - Buscar un contacto.
            ''')
            
if dec == "1":
    nomb = input("Ingrese el nombre: ")
    tel = functions.validar_numero()
    email = functions.validar_email()
    
    consultas.agregar_contacto(nomb, tel, email)
else:
    print("ERROR ABISMALISIMO")
    