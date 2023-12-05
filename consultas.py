"""
Crear clase Contacto con atributos nombre, numero y correo electronico (validar numero y correo)
Agregar metodo para agregar un contacto 
Agregar metodo que busque el contacto por nombre o numero
"""
import functions as validations
import sqlite3 as sq

conn = sq.connect("contact_list.db")
cursor = conn.cursor()
        
def inicializar_database ():
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS contactos (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           nombre TEXT,
                           telefono INTEGER,
                           email TEXT
                       )
                       ''')
        conn.commit()

def agregar_contacto(nombre, telefono, email):
    if buscar_x("nombre", nombre)[0] == 0:
        cursor.execute('''
                       INSERT INTO contactos(nombre, telefono, email)
                       VALUES (?,?,?)
                       ''',(nombre,telefono,email,))
        conn.commit()
        print(f"{nombre} agregado correctamente a la lista de contactos.")
    else:
        print(f"{nombre} ya existe en tu lista de contactos.")
        
def buscar_x(parametro,x):
    if len (x) < 3:
        print("Debes colocar más de 3 letras.")
        return
    else:
        cursor.execute(f'''
                    SELECT * FROM contactos 
                    WHERE {parametro} LIKE ?;
                   ''',(f'%{x}%',))
    res = cursor.fetchall()
    if res:
        return [1, res]
    else:
        return [0, 0]
    
        
    