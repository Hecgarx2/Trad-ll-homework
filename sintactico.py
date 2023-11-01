import re
import tkinter as tk
import grafo

# ----------Analisis sintactico-------------
# Expresión regular para identificar identificadores y constantes

error = False

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
    table = tablaSimbolos(tokens)       #Crea tabla de simbolos
    if error:
        print('Error: Token desconocido en la secuencia')
    else:
        graph = tablaGrafo(tokens)
        if error:
            print('Error: El orden esperado debe ser <oerando> <operador> <operando>')
        else:
            for column in table:
                tipo, valor = column
                print(f" | {tipo} | {valor} |")
            for node in graph:
                print(f" | {node.getOp()} | {node.getArg1()} | {node.getArg2()} |")

def tablaGrafo(tokens):
    graph = []
    cont = -1
    for token in tokens:
        tipo, valor = token
        print(f"{tipo} {valor}")
        '''cont += 1
        tipo, valor = token
        if tipo == 'IDENTIFICADOR' or  tipo == 'CONSTANTE':
            nodo = grafo.Nodo(valor, '', '')
            graph.append(nodo)
        elif tipo == 'OPERADOR':
            try:
                arg1 = tokens[cont-1]
                arg2 = tokens[cont+1]
                tipo1, valor1 = arg1
                tipo2, valor2 = arg2
                nodo = grafo.Nodo(valor, valor1, valor2)
            except:
                global error 
                error = True
                return []'''
    return graph

def tablaSimbolos(tokens):
    table = []
    for token in tokens:  # Para cada token en la cadena
        tipo, valor = token
        try:
            if table.index(token):
                print('Valor existe en la lista')
        except:
            if tipo != 'DESCONOCIDO':
                table.append(token)
            else:
                global error 
                error = True
                return []
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