import re

def validar_numero():
    patron = r'11\d{8}'
    
    while True:
        numero = input("Ingrese el numero: ")
        if re.match(patron,numero):
            return int(numero)
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