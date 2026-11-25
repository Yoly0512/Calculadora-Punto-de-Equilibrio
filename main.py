import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Calculadora de Punto de Equilibrio")
ventana.geometry("900x650")
ventana.configure(bg="#ffc0e0")

# --- TITULO ---
tk.Label(ventana, text="Calculadora de Punto de Equilibrio", font=("Arial", 22, "bold"), bg="#ffc0e0", fg="black").pack(pady=10)

# --- ENTRADAS ---
marco = tk.Frame(ventana, bg="#ffc0e0")
marco.pack()

tk.Label(marco, text="Costos Fijos ($):", bg="#ffc0e0", font=("Arial", 11)).grid(row=0, column=0)
entrada_fijos = tk.Entry(marco, font=("Arial", 11))
entrada_fijos.insert(0, "6000000")
entrada_fijos.grid(row=0, column=1, padx=5)

tk.Label(marco, text="Precio de Venta por unidad ($):", bg="#ffc0e0", font=("Arial", 11)).grid(row=0, column=2)
entrada_precio = tk.Entry(marco, font=("Arial", 11))
entrada_precio.insert(0, "100000")
entrada_precio.grid(row=0, column=3, padx=5)

tk.Label(marco, text="Costo Variable por unidad ($):", bg="#ffc0e0", font=("Arial", 11)).grid(row=0, column=4)
entrada_variable = tk.Entry(marco, font=("Arial", 11))
entrada_variable.insert(0, "40000")
entrada_variable.grid(row=0, column=5, padx=5)

# --- RESULTADO ---
label_resultado = tk.Label(ventana, text="", font=("Arial", 16, "bold"), bg="#ffc0e0", fg="black", justify="left")
label_resultado.pack(pady=10)

# --- TABLA ---
tk.Label(ventana, text="Tabla de Ganancias", font=("Arial", 14, "bold"), bg="#ffc0e0").pack()

tabla = ttk.Treeview(ventana, columns=("Unidades", "Ventas", "Utilidad"), show="headings", height=13)
tabla.heading("Unidades", text="Unidades")
tabla.heading("Ventas", text="Ventas")
tabla.heading("Utilidad", text="Utilidad")
tabla.pack(pady=5)

# --- GRAFICO ---
canvas = tk.Canvas(ventana, width=850, height=220, bg="white")
canvas.pack(pady=10)

def formato(n):
    return f"${n:,.0f}".replace(",", ".")

def calcular():
    try:
        fijos = float(entrada_fijos.get())
        precio = float(entrada_precio.get())
        variable = float(entrada_variable.get())

        if precio <= variable:
            label_resultado.config(text="El precio debe ser mayor que el costo variable")
            return

        equilibrio = fijos / (precio - variable)
        ventas_equilibrio = equilibrio * precio

        label_resultado.config(text=f"Debes vender {equilibrio:.0f} unidades\nPara ganar {formato(ventas_equilibrio)} en ventas")

        # Limpiar tabla
        for item in tabla.get_children():
            tabla.delete(item)

        # Llenar tabla de 0 a 120
        max_unidades = 120
        for u in range(0, max_unidades + 1, 10):
            ventas = u * precio
            costos = fijos + (u * variable)
            utilidad = ventas - costos
            tabla.insert("", "end", values=(u, formato(ventas), formato(utilidad)))

        # Dibujar grafico
        canvas.delete("all")
        # Ejes
        canvas.create_line(50, 10, 50, 200, width=2)
        canvas.create_line(50, 200, 830, 200, width=2)

        max_y = max_unidades * precio + 1000000
        def x_pos(u): return 50 + (u / max_unidades) * 750
        def y_pos(valor): return 200 - (valor / max_y) * 180

        # Linea Ventas (azul)
        puntos_ventas = []
        # Linea Costos Totales (rojo)
        puntos_costos = []
        for u in range(0, max_unidades + 1, 10):
            puntos_ventas.append((x_pos(u), y_pos(u * precio)))
            puntos_costos.append((x_pos(u), y_pos(fijos + u * variable)))

        canvas.create_line(puntos_ventas, fill="blue", width=2)
        canvas.create_line(puntos_costos, fill="red", width=2)
        canvas.create_text(100, 215, text="Azul = Ventas", fill="blue")
        canvas.create_text(250, 215, text="Rojo = Costos Totales", fill="red")

    except:
        label_resultado.config(text="Revisa que todos los números estén bien")

tk.Button(marco, text="Calcular", bg="white", font=("Arial", 11), command=calcular).grid(row=0, column=6, padx=10)

# Calcular al abrir
calcular()
ventana.mainloop()
