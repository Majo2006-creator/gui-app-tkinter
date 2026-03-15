# Importamos la librería tkinter
import tkinter as tk
from tkinter import messagebox

# Función para agregar datos a la lista
def agregar_dato():
    texto = entrada.get()

    if texto != "":
        lista.insert(tk.END, texto)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Ingrese un dato")

# Función para limpiar datos
def limpiar_dato():
    seleccion = lista.curselection()

    if seleccion:
        lista.delete(seleccion)
    else:
        lista.delete(0, tk.END)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI - Gestión de Datos")
ventana.geometry("400x350")

# Etiqueta
label = tk.Label(ventana, text="Ingrese información:")
label.pack(pady=10)

# Campo de texto
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=5)

# Botón agregar
btn_agregar = tk.Button(
    ventana,
    text="Agregar",
    command=agregar_dato
)
btn_agregar.pack(pady=5)

# Lista para mostrar datos
lista = tk.Listbox(ventana, width=40, height=10)
lista.pack(pady=10)

# Botón limpiar
btn_limpiar = tk.Button(
    ventana,
    text="Limpiar / Eliminar",
    command=limpiar_dato
)
btn_limpiar.pack(pady=5)

# Ejecutar aplicación
ventana.mainloop()
