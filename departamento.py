class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cola = []

    def agregar_paciente(self, paciente):
        self.cola.append(paciente)
    
    def atender_siguiente(self):
        if len(self.cola) > 0:
            return self.cola.pop(0)
        else:
            return "No hay pacientes en cola"
        
    def ver_cola(self):
        if len(self.cola)>0:
            for paciente in self.cola:
                print(paciente)
        else:
            print("la cola esta vacia")

        
