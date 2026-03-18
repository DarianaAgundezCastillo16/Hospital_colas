import tkinter as tk
from tkinter import messagebox

class Notificacion:
    def notificacion_al_paciente(self, nombre):
        messagebox.showinfo("Aviso", f"Paciente {nombre}, porfavor acuda a consulta ")