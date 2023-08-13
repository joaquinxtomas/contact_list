"""
Crear clase Contacto con atributos nombre, numero y correo electronico (validar numero y correo)
Agregar metodo para agregar un contacto 
Agregar metodo que busque el contacto por nombre o numero
"""
import re

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

def validar_numero():
    patron = r'11\d{8}'
    
    while True:
        numero = input("Ingrese el numero: ")
        
        if re.match(patron,numero):
            return numero
        else:
            print("Numero inválido!\n")
            
def validar_email():
    patron = r'[a-zA-Z0-9]{1,}@[a-zA-Z]{1,}\.[a-zA-Z]'
    
    while True:
        email = input("Ingrese el email: ")
        
        if re.match(patron, email):
            return email
        else:
            print("Esto es incorrecto")
            
contactos = []
contacto_nuevo = (Contacto("","",""))

while True:

    busqueda = input("Ingrese el nombre o el numero de el contacto a buscar: ")
    
    
    if(contacto_nuevo.buscar_x(contactos,busqueda)):
        print(f'\n----------------\nNombre: {contacto_nuevo.nombre}\nNumero: {contacto_nuevo.telefono}\nEmail: {contacto_nuevo.email}\n----------------\n')
    else:
        print("\n----------------\nNo se ha encontrado el contacto. Vamos a agregarlo.\n")
        nombre = input("Ingrese su nombre: ")
        numero = validar_numero()
        email = validar_email()
        contacto_nuevo = Contacto(nombre,numero,email)
        contacto_nuevo.agregar_contacto(contactos)
        
    
        
    