# controllers/MesaController.py
from models.Mesa import Mesa

class MesaController:
    def __init__(self):
        self.mesas = []
        self.next_id = 1

    def agregar_mesa(self, capacidad):
        mesa = Mesa(self.next_id, capacidad)
        self.mesas.append(mesa)
        self.next_id += 1
        return mesa

    def buscar_mesa(self, id_mesa):
        for mesa in self.mesas:
            if mesa.id_mesa == id_mesa:
                return mesa
        return None

    def mesas_disponibles(self, fecha, hora, num_personas):
        # En una implementación real, aquí se verificarían las reservas existentes
        # para esa fecha y hora, pero como ejemplo simplificado:
        return [mesa for mesa in self.mesas 
                if mesa.capacidad >= num_personas 
                and mesa.estado == "disponible"]

    def liberar_mesa(self, id_mesa):
        mesa = self.buscar_mesa(id_mesa)
        if mesa:
            mesa.liberar()
            return True
        return False