# models/Reserva.py
class Reserva:
    def __init__(self, id_reserva, cliente, mesa, fecha, hora, num_personas, estado="confirmada"):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.mesa = mesa
        self.fecha = fecha
        self.hora = hora
        self.num_personas = num_personas
        self.estado = estado

    def modificar(self, nueva_mesa=None, nueva_fecha=None, nueva_hora=None, nuevo_num_personas=None):
        if nueva_mesa:
            self.mesa.liberar()
            self.mesa = nueva_mesa
            nueva_mesa.ocupar()
        if nueva_fecha:
            self.fecha = nueva_fecha
        if nueva_hora:
            self.hora = nueva_hora
        if nuevo_num_personas:
            self.num_personas = nuevo_num_personas

    def cancelar(self):
        self.estado = "cancelada"
        self.mesa.liberar()

    def __str__(self):
        return f"Reserva #{self.id_reserva} - {self.cliente.nombre} - {self.fecha} {self.hora} - Mesa {self.mesa.id_mesa}"