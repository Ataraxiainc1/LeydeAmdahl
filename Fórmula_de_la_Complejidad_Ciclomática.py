# -*- coding: latin-1 -*-
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

def generar_imagen_formula():
    # Definir la fórmula en TEX
    formula_tex = r"$M = E - N + 2P$"

    # Configurar Matplotlib para renderizar texto en TEX
    plt.rcParams["text.usetex"] = True

    # Crear la figura y el eje
    fig, ax = plt.subplots(figsize=(4, 2.5))

    # Renderizar la fórmula en el eje
    ax.text(0.5, 0.35, formula_tex, fontsize=18, ha="center", va="center")

    # Eliminar los ejes
    ax.axis("off")

    # Guardar la figura como imagen
    fig.savefig("formula_temp.png", dpi=300, bbox_inches="tight", pad_inches=0)

    # Cerrar la figura
    plt.close(fig)

    # Abrir la imagen guardada
    image = Image.open("formula_temp.png")

    # Recortar la imagen
    bbox = image.getbbox()
    cropped_image = image.crop(bbox)

    # Guardar la imagen recortada
    cropped_image.save("formula.png")
    

    # Cargar la imagen de la fórmula
    formula_image = Image.open("formula.png")

    # Recortar la imagen con un margen adicional
    left = 150
    top = 300
    right = formula_image.width - 150
    bottom = formula_image.height - 150
    cropped_image = formula_image.crop((left, top, right, bottom))

    # Guardar la imagen recortada
    cropped_image.save("formula_recortada.png")


    # Eliminar la imagen temporal
    image.close()
    cropped_image.close()

def calcular_complejidad():
    num_arcos = int(entry_arcos.get())
    num_nodos = int(entry_nodos.get())
    num_componentes = int(entry_componentes.get())
    
    complejidad = num_arcos - num_nodos + 2 * num_componentes
    
    label_resultado.config(text=f"Complejidad Ciclomática: {complejidad}")

# Crear la ventana principal
window = tk.Tk()
window.title("Calculadora de Complejidad Ciclomática")

# Configurar estilo temático para el modo oscuro
style = ttk.Style()
style.theme_use('clam')  # Puedes probar con otros temas disponibles: 'clam', 'alt', 'default', etc.
style.configure('.', foreground='light green', background='black', font=('Arial', 14, "bold"), fieldbackground='black')
style.configure('Resultado.TLabel', foreground='orange')  # Configurar el color naranja para el label_resultado

# Configurar color de fondo para la ventana principal
window.configure(bg='black')

# Agregar un resumen de la fórmula
resumen_formula = "La Complejidad Ciclomática se calcula mediante la fórmula: \n\nM = E - N + 2P\n\nDonde:\n- E es el número de arcos\n- N es el número de nodos\n- P es el número de componentes conexos\n\nLa Complejidad Ciclomática es una medida de la complejidad estructural de un programa."
label_resumen = ttk.Label(window, text=resumen_formula, justify="left", font=('Arial', 16, "bold"))
label_resumen.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

# Generar la imagen de la fórmula
generar_imagen_formula()

# Cargar la imagen de la fórmula
formula_image = Image.open("formula_recortada.png")
formula_photo = ImageTk.PhotoImage(formula_image)

formula_photo = ImageTk.PhotoImage(formula_image)

# Crear los elementos de la interfaz
label_formula = ttk.Label(window, image=formula_photo)
label_formula.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

label_arcos = ttk.Label(window, text="Número de Arcos:", font=('Arial', 16, 'bold'))
entry_arcos = ttk.Entry(window, font=('Arial', 16))
label_nodos = ttk.Label(window, text="Número de Nodos:", font=('Arial', 16, 'bold'))
entry_nodos = ttk.Entry(window, font=('Arial', 16))
label_componentes = ttk.Label(window, text="Número de Componentes Conexos:", font=('Arial', 16, 'bold'))
entry_componentes = ttk.Entry(window, font=('Arial', 16))
btn_calcular = tk.Button(window, text="Calcular", command=calcular_complejidad, font=('Arial', 16, 'bold'))
label_resultado = ttk.Label(window, text="Complejidad Ciclomática: ", font=('Arial', 16, 'italic'), style='Resultado.TLabel')

# Posicionar los elementos en la ventana
label_arcos.grid(row=2, column=0, padx=16, pady=5)
entry_arcos.grid(row=2, column=1, padx=10, pady=5)
label_nodos.grid(row=3, column=0, padx=10, pady=5)
entry_nodos.grid(row=3, column=1, padx=10, pady=5)
label_componentes.grid(row=4, column=0, padx=10, pady=5)
entry_componentes.grid(row=4, column=1, padx=10, pady=5)
btn_calcular.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
label_resultado.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# Ejecutar la ventana
window.mainloop()