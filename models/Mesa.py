# models/Mesa.py
class Mesa:
    def __init__(self, id_mesa, capacidad, estado="disponible"):
        self.id_mesa = id_mesa
        self.capacidad = capacidad
        self.estado = estado

    def ocupar(self):
        self.estado = "ocupada"

    def liberar(self):
        self.estado = "disponible"

    def __str__(self):
        return f"Mesa {self.id_mesa} (Capacidad: {self.capacidad}, Estado: {self.estado})"