import re
import tkinter as tk
import grafo
import tabla

# ----------Analisis sintactico-------------
# Expresión regular para identificar identificadores y constantes

Error = False

token_specification = [
    ('IDENTIFICADOR', r'[a-zA-Z]'),  # Identificador
    ('CONSTANTE', r'\d+'),  # Constante
    ('OPERADOR', r'[+\-*/]'),  # Operador
    ('ESPACIO', r'\s+'),    # Espacios en blanco
    ('DESCONOCIDO', r'[^a-zA-Z0-9\s]')     # Desconocido
]

# Combinar las especificaciones de tokens en una expresión regular
master_pattern = re.compile('|'.join('(?P<%s>%s)' % pair for pair in token_specification))

def validarToken(expression):
    for token in re.finditer(master_pattern, expression):
        tipo = token.lastgroup      # Tipo
        valor = token.group()       # Valor
        if tipo != 'ESPACIO':
            yield tipo, valor

def sintactico():
    expresion = cadena.get()
    tokens = validarToken(expresion)
    table = tablaSimbolos(tokens)
    
    for column in table:
        print(f" | {column.getTipo()} | {column.getVal()} |")

def tablaSimbolos(tokens):
    table = []
    for token in tokens:  # Para cada token en la cadena
        tipo, valor = token
        if tipo != 'DESCONOCIDO':
            columna = tabla.Columns(tipo, valor)
            table.append(columna)
        else:
            print(f"Error token desconocido encontrado: {valor}")
    return table

# ----------Interfaz-------------
root = tk.Tk()

root.title("Practica 3")
root.config(width=250, height=200)

cadena = tk.Entry(root)
cadena.place(x=10, y=60)

btnVer = tk.Button(root, text="Analizar", command= sintactico)
btnVer.place(x=10, y=20)

root.mainloop()