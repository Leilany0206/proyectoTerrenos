import tkinter as tk
from tkinter import messagebox, Toplevel, Label, Button 
from pprintpp import pprint

aux_line = '' # Inicializa un auxiliar que guarde cada linea en with open

# LECTURA DE TXT
try:
    with open('C:/Users/980025550/Downloads/Software/introProgramacion/proyectoTerrenos/solar.txt', 'r', encoding='utf-8') as archive:
        for line in archive:
            aux_line += line
except FileNotFoundError: # Atrapa el error de no encontrar el archivo
    print('El archivo no se encontró') 

solar = eval(aux_line) # Evalúa la estructura del string en formato de diccionario [1]
pprint(solar)

# TK VENTANA
root = tk.Tk() 
root.title('Bienes raíces')

# LABEL
root_description = Label(root, text = 'Gracias por su interes en adquirir un solar \n Los solares en rojo son aquellos que ya fueron vendidos, los verdes están disponibles')
root_description.pack()

# FRAME
frame = tk.Frame(root, width=600, height=600, bg="lightgray")
frame.pack() 
# CORREGIR

# PESTAÑA (3) QUE CONFIRMA LA COMPRA
def confirm_purchase(i):  
     
    top3 = Toplevel() # Crea widget
    top3.title('Compra') # Establece título del widget
    top3.geometry('200x100') # Establece tamaño

    label_confirm = Label(top3, text = "¡Gracias por su compra!") # Crea la leyenda
    button_confirm = Button(top3, text = "Salir", command=top3.destroy) # Botón para confirmar compra

    label_confirm.pack() 
    button_confirm.pack()
     
    # Display hasta su cierre 
    top3.mainloop()

# PESTAÑA (2) QUE PIDE EL NOMBRE DEL COMPRADOR
def open_purchase(i):  
     
    top2 = Toplevel() # Crea widget
    top2.title('Compra') # Establece título del widget
    top2.geometry('200x100') # Establece tamaño

    label_purchase = Label(top2, text = "Por favor ingrese su nombre: ") # Crea la leyenda
    entry_purchase = tk.Entry(top2, width=30) # Input para colocar el nombre
    button_purchase = Button(top2, text = "Confirmar", command=lambda i=i: [name_purchase(i), confirm_purchase(i)]) # Botón para confirmar compra y abrir la ventana 3 [3]
    button_close_purchase = Button(top2, text = "Salir", command=top2.destroy) #Botón para cerrar

    # FUNCIÓN QUE MANEJA LA LÓGICA DE ESCRIBIR EL NOMBRE DEL COMPRADOR
    def name_purchase(i):
        solar[i]["comprador"] = entry_purchase.get()
    # SOBRESCRIBE EL ARCHIVO TXT
        try:
            with open('C:/Users/980025550/Downloads/Software/introProgramacion/proyectoTerrenos/solar.txt', "w", encoding='utf-8') as archive:
                archive.write(str(solar))
        except FileNotFoundError: # Atrapa el error de no encontrar el archivo
            print('El archivo no se encontró') 
     
    # Monta todos los componentes
    label_purchase.pack() 
    entry_purchase.pack()
    button_purchase.pack()
    button_close_purchase.pack()
     
    # Display hasta su cierre 
    top2.mainloop()

# FUNCIÓN PARA MOSTRAR INFO DE CADA TERRENO :) [2]
def show_info(i): 
    aux_info = f'Tamaño: {solar[i]["tamaño"]} \n Precio: {solar[i]["precio"]}' # F string que muestra el value del key especificado
    if solar[i]["comprador"] != '': # Si el value de comprador no es un str vacío lo muestra
        aux_info += f'\n Comprado por: {solar[i]["comprador"]}'
    return aux_info

# PESTAÑA (1) QUE ABRE LA INFORMACIÓN DEL TERRENO
def open_info(i):  
     
    top1 = Toplevel(root) # Crea widget
    top1.title('Información del solar') # Establece título del widget
    top1.geometry('200x100') # Establece tamaño

    label_info = Label(top1, text = show_info(i)) # Crea la leyenda
    button_close_info = Button(top1, text = "Cerrar", command = top1.destroy) # Botón para cerrar la ventana
    button_open_purchase = Button(top1, text = "Comprar", command=lambda i=i: open_purchase(i)) # Botón para comprar
    
    # Si no existe comprador, da la opción de comprar, si ya tiene, sólo monta el botón de salir
    label_info.pack() 
    if solar[i]["comprador"] == '': 
        button_open_purchase.pack()
        button_close_info.pack()
    elif solar[i]["comprador"] != '':
        button_close_info.pack()

    # Display hasta su cierre 
    top1.mainloop()

# ESPACIO PARA CADA TERRENO
x = 0 # Posiciona los rows
y = 0 # Posiciona los columns

# ENCERRAR ESTO EN UNA FUNCIÓN PARA REUTILIZARLA 
for i in solar:

    def change_color(i):
        if solar[i]['comprador'] != '': return 'red'
        else: return 'green'

    aux_button = tk.Button(frame, text=f'{i}', command=lambda i=i: open_info(i), bg=change_color(i), width=10, height=10)
    aux_button.grid(row=x, column=y)

    y += 1 # Con cada iteración aumenta 1 la columna

    if (i % 3) == 0: # Cuando el contador (Número de solar) llega a 3, pasa lo siguiente para que se tome como argumentos en la siguiente iteración:
        x += 1 # El row aumenta 1
        y = 0 # La columna regresa a 0

# MAINLOOP: Levanta la ventana
root.mainloop() 

''' DOCUMENTACIÓN
[1] https://thedataschools.com/python/funciones/eval-funcion/#:~:text=La%20funci%C3%B3n%20eval()%20en,c%C3%B3digo%20y%20devolviendo%20el%20resultado.
[2] https://www.geeksforgeeks.org/python-tkinter-toplevel-widget/
[3] https://www.geeksforgeeks.org/how-to-bind-multiple-commands-to-tkinter-button/
'''