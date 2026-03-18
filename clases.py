class Cola_Prioridad:
    def __init__(self):
        self.paciente = [] #guradamos los diccionarios de paciente

    def prioridad_medica(self, paciente):
        #añadir paciente a la lista
        self.paciente.append(paciente)
        
        # Ordenamos: primero por nivel de prioridad, 
        # y si son iguales, por la fecha de ingreso (FIFO)
        self.paciente.sort(key = lambda x: (x['Prioridad'], x['Fecha']))
        print(f"Paciente {paciente['Nombre']} encolado")

    def fecha_ingreso(self, paciente):
        #registrar hora de salida
        hora_salida = datatime.now().isoformat()

  class Gestor_Estadistica:
    def tiempo_promedio(self, paciente): # Agregamos self y paciente
        # 1. Convertimos el texto del JSON a formato de fecha real
        entrada = datetime.fromisoformat(paciente['Fecha'])
        salida = datetime.now()
        
        # 2. Calculamos la diferencia
        diferencia = salida - entrada
        total_segundos = int(diferencia.total_seconds())
        
        # 3. Usamos // para calcular minutos y segundos
        minutos = total_segundos // 60
        segundos_restantes = total_segundos % 60
        
        print(f"El paciente estuvo {minutos} min y {segundos_restantes} seg en espera.")
        return total_segundos
