import json
from datetime import datetime

class Paciente:
    PRIORIDADES = {1: "Emergencia", 2: "Urgente", 3: "Normal"}

    def __init__(self):
        self.nombre = ""
        self.fecha = ""
        self.edad = ""
        self.genero = ""
        self.nacionalidad = ""
        self.estado_civil = ""
        self.telefono = ""
        self.correo = ""
        self.numero = ""
        self.peso = 0.0
        self.estatura = 0.0
        self.imc = 0.0
        self.prioridad = 3
        self.departamento = "Medicina General"
        self.hora_registro = datetime.now()
        self.hora_atencion = None

    def registrar_paciente(self):
        print("\n── Registro de Paciente ──────────────────────")
        self.nombre = input("Ingrese el nombre del paciente: ").strip().title()
        self.fecha = datetime.now().isoformat()
        self.edad = input("Ingrese la edad: ")
        self.genero = input("Ingrese el género: ")
        self.nacionalidad = input("Ingrese la nacionalidad: ")
        self.estado_civil = input("Ingrese el estado civil: ")
        self.telefono = input("Ingrese teléfono: ")
        self.correo = input("Ingrese correo: ")
        self.numero = input("Ingrese número de expediente: ")
        
        try:
            self.peso = float(input("Ingrese el peso (Kg): "))
            self.estatura = float(input("Ingrese la estatura (cm): "))
            # IMC = peso / estatura(m)^2
            estatura_m = self.estatura / 100
            self.imc = round(self.peso / (estatura_m ** 2), 2)
        except ValueError:
            print("Error: Ingrese valores numéricos para peso y estatura.")

        print("\nNiveles: 1: Emergencia, 2: Urgente, 3: Normal")
        self.prioridad = int(input("Seleccione nivel de prioridad (1-3): ") or 3)

        datos = {
            "Nombre": self.nombre,
            "Fecha": self.fecha,
            "Edad": self.edad,
            "Genero": self.genero,
            "Nacionalidad": self.nacionalidad,
            "Estado Civil": self.estado_civil,
            "Telefono": self.telefono,
            "Correo": self.correo,
            "Numero": self.numero,
            "Estatura": self.estatura,
            "Peso_Kg": self.peso,
            "IMC": self.imc,
            "Prioridad": self.prioridad,
            "Departamento": self.departamento
        }

        with open("datos.json", "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

        print(f"\n Registro completo: {self.nombre} | IMC: {self.imc}")

    def llamar_siguiente(self):
        self.hora_atencion = datetime.now()
        print(f"\n NOTIFICACIÓN: Paciente {self.nombre}, pase al consultorio de {self.departamento}.")

    def __lt__(self, other):
        # Lógica para la cola de prioridad
        if self.prioridad != other.prioridad:
            return self.prioridad < other.prioridad
        return self.hora_registro < other.hora_registro

    def __str__(self):
        return f"[{self.PRIORIDADES[self.prioridad]}] {self.nombre} - Expediente: {self.numero}"

class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cola = []

    def agregar_paciente(self, paciente):
        paciente.departamento = self.nombre
        self.cola.append(paciente)
        # Ordenar automáticamente por prioridad y luego por llegada
        self.cola.sort()

    def atender_siguiente(self):
        if self.cola:
            paciente = self.cola.pop(0)
            paciente.llamar_siguiente()
            return paciente
        return None

    def ver_cola(self):
        print(f"\n--- Cola en {self.nombre} ---")
        if not self.cola:
            print("No hay pacientes esperando.")
        for p in self.cola:
            print(p)

class Gestor_Estadistica:
    def __init__(self):
        self.tiempos_espera = []

    def calcular_y_mostrar(self, paciente):
        if paciente.hora_atencion:
            entrada = datetime.fromisoformat(paciente.fecha)
            salida = paciente.hora_atencion
            diferencia = salida - entrada
            
            total_segundos = int(diferencia.total_seconds())
            minutos = total_segundos // 60
            segundos = total_segundos % 60
            
            self.tiempos_espera.append(total_segundos)
            print(f"⏱️ Tiempo de espera de {paciente.nombre}: {minutos} min y {segundos} seg.")
        else:
            print("El paciente aún no ha sido atendido.")

# --- EJEMPLO DE USO DEL SISTEMA ---
if __name__ == "__main__":
    # 1. Creamos el hospital y el gestor
    area_urgencias = Departamento("Urgencias")
    estadisticas = Gestor_Estadistica()

    # 2. Registramos un paciente (esto pedirá inputs)
    p1 = Paciente()
    p1.registrar_paciente()
    area_urgencias.agregar_paciente(p1)

    # 3. Ver cola
    area_urgencias.ver_cola()

    # 4. Atender y generar estadística
    atendido = area_urgencias.atender_siguiente()
    if atendido:
        estadisticas.calcular_y_mostrar(atendido)
