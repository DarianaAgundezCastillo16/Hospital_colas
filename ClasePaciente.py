import json
from datetime import datetime


class Paciente:

    PRIORIDADES = {1: " Emergencia", 2: " Urgente", 3: " Normal"}

    def __init__(self):
        self.nombre        = ""
        self.fecha         = ""
        self.edad          = ""
        self.genero        = ""
        self.nacionalidad  = ""
        self.estado_civil  = ""
        self.telefono      = ""
        self.correo        = ""
        self.numero        = ""
        self.peso          = 0.0
        self.estatura      = 0.0
        self.imc           = 0.0
        self.prioridad     = 3
        self.departamento  = "Medicina General"
        self.hora_registro = datetime.now()
        self.hora_atencion = None

    def registrar_paciente(self):
        """
        Solicita los datos del paciente por input y guarda en datos.json.
        Calcula el IMC automáticamente (peso kg / estatura m²).
        """
        print("\n── Registro de Paciente ──────────────────────")

        self.nombre       = input("Ingrese el nombre del paciente: ").strip().title()
        self.fecha        = datetime.now().isoformat()
        self.edad         = input("Ingrese la edad del paciente: ")
        self.genero       = input("Ingrese el genero del paciente: ")
        self.nacionalidad = input("Ingrese la nacionalidad del paciente: ")
        self.estado_civil = input("Ingrese el estado civil del paciente: ")
        self.telefono     = input("Ingrese un numero de telefono: ")
        self.correo       = input("Ingrese un correo: ")
        self.numero       = input("Ingrese número de expediente: ")

        self.peso     = float(input("Ingrese el peso del paciente en Kg: "))
        self.estatura = float(input("Ingrese la estatura del paciente en cm: "))

        # IMC = peso(kg) / (estatura en metros)²
        estatura_m = self.estatura / 100
        self.imc = round(self.peso / (estatura_m ** 2), 2)

        self.hora_registro = datetime.now()

        datos = {
            "Nombre":       self.nombre,
            "Fecha":        self.fecha,
            "Edad":         self.edad,
            "Genero":       self.genero,
            "Nacionalidad": self.nacionalidad,
            "Estado Civil": self.estado_civil,
            "Telefono":     self.telefono,
            "Correo":       self.correo,
            "Numero":       self.numero,
            "Estatura":     self.estatura,
            "Peso_Kg":      self.peso,
            "IMC":          self.imc,
        }

        with open("datos.json", "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

        print(f"\n Paciente registrado: {self.nombre} | IMC: {self.imc} | "
              f"{Paciente.PRIORIDADES[self.prioridad]} | {self.departamento}")
        print(" Archivo datos.json creado")

    def __str__(self):
        return (f"--- Datos del Paciente ---\n"
                f"Fecha: [{self.fecha}] - Nombre: {self.nombre} - "
                f"Edad: {self.edad} - Genero: {self.genero}\n"
                f"Nacionalidad: {self.nacionalidad}\n"
                f"Estado Civil: {self.estado_civil}\n"
                f"Telefono:     {self.telefono}\n"
                f"Correo:       {self.correo}")

    def reservar_cita(self, fecha_futura: datetime) -> str:
        """No se pueden reservar fechas anteriores a hoy."""
        if fecha_futura < datetime.now():
            return (f" No se pueden reservar fechas anteriores. "
                    f"Fecha recibida: {fecha_futura.strftime('%d/%m/%Y %H:%M')}")
        self.hora_registro = fecha_futura
        return (f" Cita reservada para {self.nombre} "
                f"el {fecha_futura.strftime('%d/%m/%Y %H:%M')}")

    def llamar_siguiente(self):
        """Marca la hora de atencion y notifica al paciente."""
        self.hora_atencion = datetime.now()
        print(f"NOTIFICACION: Paciente {self.nombre}, "
              f"por favor acuda a su consultorio en {self.departamento}.")

    def paciente_anterior(self):
        """Muestra la información del paciente."""
        print(f"  Nombre        : {self.nombre}")
        print(f"  Fecha registro: {self.fecha}")
        print(f"  Edad          : {self.edad}")
        print(f"  Género        : {self.genero}")
        print(f"  Nacionalidad  : {self.nacionalidad}")
        print(f"  Estado Civil  : {self.estado_civil}")
        print(f"  Teléfono      : {self.telefono}")
        print(f"  Correo        : {self.correo}")
        print(f"  Número        : {self.numero}")
        print(f"  Peso/Estatura : {self.peso} kg / {self.estatura} cm")
        print(f"  IMC           : {self.imc}")
        print(f"  Prioridad     : {Paciente.PRIORIDADES[self.prioridad]}")
        print(f"  Departamento  : {self.departamento}")
        print(f"  Atendido      : {self.hora_atencion.strftime('%d/%m/%Y %H:%M:%S') if self.hora_atencion else 'Pendiente'}")

    def __lt__(self, other):
        if self.prioridad != other.prioridad:
            return self.prioridad < other.prioridad
        return self.hora_registro < other.hora_registro

    def __repr__(self):
        return (f"Paciente({self.nombre!r}, #{self.numero}, "
                f"{Paciente.PRIORIDADES[self.prioridad]}, {self.departamento})")
