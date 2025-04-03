import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class recta:
    def __init__(self, root):
        self.root = root
        self.root.title("Gráficas de recta")
        
        self.valores_frame = tk.Frame(root)
        self.valores_frame.pack(side="left", padx=20)
        
        self.pendiente_label = tk.Label(self.valores_frame, text="Ingresa el valor de la pendiente")
        self.pendiente_label.pack()
        self.pendiente_entry = tk.Entry(self.valores_frame)
        self.pendiente_entry.pack()
        
        self.independiente_label = tk.Label(self.valores_frame, text="Ingresa el valor de la variable independiente (b)")
        self.independiente_label.pack()
        self.independiente_entry = tk.Entry(self.valores_frame)
        self.independiente_entry.pack()
        
        self.graficar = tk.Button(self.valores_frame, text="Graficar", command=self.graficar)
        self.graficar.pack()
        
        self.grafica = tk.Frame(root)
        self.grafica.pack(side="right", padx=20)
        
    def graficar(self):
        try:
            m = float(self.pendiente_entry.get())
            b = float(self.independiente_entry.get())
            
            x = np.linspace(-5, 5, 400)
            y = m * x + b
            
            fig, ax = plt.subplots()
            ax.plot(x, y, color='red', label=f'Recta: y = {m}x + {b}')  # Línea roja
            ax.axhline(0, color='black', linewidth=0.5)
            ax.axvline(0, color='black', linewidth=0.5)
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.set_xlim(-5, 5)  # Rango de -5 a 5 en el eje x
            ax.grid(True)
            ax.legend()
            
            for widget in self.grafica.winfo_children():
                widget.destroy()

            canvas = FigureCanvasTkAgg(fig, master=self.grafica)
            canvas.draw()
            canvas.get_tk_widget().pack()
            
        except ValueError:
            messagebox.showerror("Error", "Ingresa un valor numérico válido")

if __name__ == "__main__":
    root = tk.Tk()
    app = recta(root)
    root.mainloop()