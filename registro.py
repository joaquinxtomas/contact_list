"""
Crear clase Contacto con atributos nombre, numero y correo electronico (validar numero y correo)
Agregar metodo para agregar un contacto 
Agregar metodo que busque el contacto por nombre o numero
"""
import functions as validations

class Contacto:
    def __init__(self, nombre,telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
    
    def agregar_contacto(self,array):
        array.append((self.nombre,self.telefono,self.email))
        return array
    
    def buscar_x(self,array,x):
        for tupla in array:
            if x in tupla:
                self.nombre,self.telefono,self.email = tupla
                return True
        return False
            
contactos = []
contacto_nuevo = (Contacto("","",""))

while True:

    busqueda = input("Ingrese el nombre o el numero de el contacto a buscar: ")
    
    
    if(contacto_nuevo.buscar_x(contactos,busqueda)):
        print(f'\n----------------\nNombre: {contacto_nuevo.nombre}\nNumero: {contacto_nuevo.telefono}\nEmail: {contacto_nuevo.email}\n----------------\n')
    else:
        print("\n----------------\nNo se ha encontrado el contacto. Vamos a agregarlo.\n")
        nombre = input("Ingrese su nombre: ")
        numero = validations.validar_numero()
        email = validations.validar_email()
        contacto_nuevo = Contacto(nombre,numero,email)
        contacto_nuevo.agregar_contacto(contactos)
        
    
        
    