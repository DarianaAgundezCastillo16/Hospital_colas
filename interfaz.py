import tkinter as tk
from tkinter import ttk, messagebox
from departamento import Departamento
from notificacion import Notificacion

# Colores
BG = "#37474F"
BTN = "#0288D1"
BTN_HOVER = "#0277BD"
BLANCO = "#FFFFFF"
CAMPO = "#D3E1E7"
TEXTO_OSCURO = "#1a1a2e"

ventana = tk.Tk()
ventana.title("Sistema de Hospital")
ventana.geometry("430x620")
ventana.configure(bg=BG)
ventana.resizable(True, True)

# Fuente
FUENTE = ("Helvetica", 11)
FUENTE_TITULO = ("Helvetica", 16, "bold")
FUENTE_BTN = ("Helvetica", 11, "bold")

# Título
tk.Label(ventana, text="🏥 Sistema de Gestion Medica",
         font=FUENTE_TITULO, bg=BG, fg=BLANCO).pack(pady=15)

# Separador
tk.Frame(ventana, bg=BLANCO, height=2).pack(fill="x", padx=20)

# Selector departamento
tk.Label(ventana, text="Departamento:", font=FUENTE, bg=BG, fg=BLANCO).pack(pady=(10,2))
depto_var = tk.StringVar(value="Pediatria")

style = ttk.Style()
style.theme_use("clam")
style.configure("TCombobox", fieldbackground=CAMPO, background=CAMPO,
                foreground=TEXTO_OSCURO, arrowcolor=BTN, font=FUENTE, padding=5)
style.map("TCombobox", background=[("readonly", CAMPO)])

departamentos = {
    "Pediatria": Departamento("Pediatria"),
    "Cardiologia": Departamento("Cardiologia"),
    "Ginecologia": Departamento("Ginecologia"),
    "Urgencias": Departamento("Urgencias")
}
notif = Notificacion()

selector = ttk.Combobox(ventana, textvariable=depto_var,
                        values=list(departamentos.keys()),
                        state="readonly", width=25, font=FUENTE)
selector.pack(pady=5)

# Frame agregar
frame_agregar = tk.LabelFrame(ventana, text=" Agregar Paciente ",
                               font=FUENTE, bg=BG, fg=BLANCO,
                               bd=2, relief="groove", padx=15, pady=10)
frame_agregar.pack(fill="x", padx=20, pady=10)

tk.Label(frame_agregar, text="Nombre:", font=FUENTE, bg=BG, fg=BLANCO).grid(row=0, column=0, padx=5)
entrada_nombre = tk.Entry(frame_agregar, bg=CAMPO, font=FUENTE,
                          relief="flat", bd=5, width=22)
entrada_nombre.grid(row=0, column=1, padx=5)

def agregar():
    nombre = entrada_nombre.get().strip()
    if nombre:
        depto = departamentos[depto_var.get()]
        depto.agregar_paciente(nombre)
        entrada_nombre.delete(0, tk.END)
        mostrar_cola()

entrada_nombre.bind("<Return>", lambda e: agregar())

tk.Button(frame_agregar, text="➕ Agregar Paciente",
          command=agregar, bg=BTN, fg=BLANCO,
          font=FUENTE_BTN, relief="flat", padx=10, pady=6, cursor="hand2").grid(row=1, column=0, columnspan=2, pady=10, sticky="ew")

# Frame gestion
frame_atender = tk.LabelFrame(ventana, text=" Gestion de Cola ",
                               font=FUENTE, bg=BG, fg=BLANCO,
                               bd=2, relief="groove", padx=15, pady=10)
frame_atender.pack(fill="x", padx=20, pady=5)

def atender():
    depto = departamentos[depto_var.get()]
    siguiente = depto.atender_siguiente()
    if siguiente != "No hay pacientes en cola":
        notif.notificacion_al_paciente(siguiente)
        mostrar_cola()
    else:
        messagebox.showinfo("Aviso", "No hay pacientes en cola")

tk.Button(frame_atender, text="✅ Atender Siguiente",
          command=atender, bg=BTN, fg=BLANCO,
          font=FUENTE_BTN, relief="flat", padx=10, pady=6, cursor="hand2").pack(fill="x")

# Cola
tk.Label(ventana, text="Pacientes en espera:", font=FUENTE, bg=BG, fg=BLANCO).pack(pady=(10,2))
area_cola = tk.Text(ventana, height=7, width=40, bg=CAMPO,
                    font=FUENTE, relief="flat", bd=5)
area_cola.pack(padx=20)

def mostrar_cola():
    area_cola.delete("1.0", tk.END)
    depto = departamentos[depto_var.get()]
    if len(depto.cola) == 0:
        area_cola.insert(tk.END, "No hay pacientes en espera")
    else:
        for i, paciente in enumerate(depto.cola, 1):
            area_cola.insert(tk.END, f"{i}. {paciente}\n")

tk.Button(ventana, text="🔍 Ver Cola",
          command=mostrar_cola, bg=BTN, fg=BLANCO,
          font=FUENTE_BTN, relief="flat", padx=15, pady=6, cursor="hand2").pack(pady=10)

ventana.mainloop()