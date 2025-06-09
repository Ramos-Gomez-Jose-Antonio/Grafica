import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GraficadorRectas:
    def __init__(self, master):
        self.master = master
        master.title("Visualizador de Ecuaciones Lineales")
        
        self.marco_entrada = tk.LabelFrame(master, text="Parámetros de la recta", padx=10, pady=10)
        self.marco_entrada.pack(side=tk.LEFT, padx=15, pady=15)
        
        tk.Label(self.marco_entrada, text="Pendiente (m):").grid(row=0, column=0)
        self.entrada_pendiente = tk.Entry(self.marco_entrada)
        self.entrada_pendiente.grid(row=0, column=1)
        
        tk.Label(self.marco_entrada, text="Ordenada al origen (b):").grid(row=1, column=0)
        self.entrada_ordenada = tk.Entry(self.marco_entrada)
        self.entrada_ordenada.grid(row=1, column=1)
        
        self.boton_graficar = tk.Button(self.marco_entrada, text="Dibujar Recta", 
                                       command=self.dibujar_recta, bg="#4CAF50", fg="white")
        self.boton_graficar.grid(row=2, columnspan=2, pady=10)
        
        self.marco_grafica = tk.Frame(master)
        self.marco_grafica.pack(side=tk.RIGHT, padx=15, pady=15)
        
        self.fig, self.ax = plt.subplots(figsize=(5, 5))
        self.configurar_grafica()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.marco_grafica)
        self.canvas.get_tk_widget().pack()
    
    def configurar_grafica(self):
        self.ax.clear()
        self.ax.axhline(0, color='gray', linewidth=1)
        self.ax.axvline(0, color='gray', linewidth=1)
        self.ax.set_xlim(-6, 6)
        self.ax.set_ylim(-6, 6)
        self.ax.grid(True, linestyle='--', alpha=0.7)
        self.ax.set_title("Gráfica de la Recta")
        self.ax.set_xlabel("Eje X")
        self.ax.set_ylabel("Eje Y")
    
    def dibujar_recta(self):
        try:
            m = float(self.entrada_pendiente.get())
            b = float(self.entrada_ordenada.get())
            
            self.configurar_grafica()
            
            x = np.linspace(-6, 6, 500)
            y = m * x + b
            
            color = "#FF5733"  # Color naranja
            self.ax.plot(x, y, color=color, linewidth=2, label=f'y = {m:.2f}x + {b:.2f}')
            self.ax.legend(loc='upper right')
            
            if -6 <= b <= 6:
                self.ax.plot(0, b, 'o', color=color, markersize=8)
                self.ax.text(0.2, b+0.2, f'(0, {b:.1f})', color=color)
            
            self.canvas.draw()
            
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos")

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = GraficadorRectas(ventana_principal)
    ventana_principal.mainloop()