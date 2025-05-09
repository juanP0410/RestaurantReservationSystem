# models/Cliente.py
class Cliente:
    def __init__(self, id_cliente, nombre, email, telefono=None):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.reservas = []  # Historial de reservas

    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)

    def obtener_reservas(self):
        return self.reservas

    def __str__(self):
        return f"{self.nombre} ({self.email})"