# controllers/ReservaController.py
from models.Reserva import Reserva
from utils.EmailSender import enviar_email_confirmacion

class ReservaController:
    def __init__(self, cliente_controller, mesa_controller):
        self.reservas = []
        self.next_id = 1
        self.cliente_controller = cliente_controller
        self.mesa_controller = mesa_controller

    def crear_reserva(self, id_cliente, id_mesa, fecha, hora, num_personas):
        cliente = self.cliente_controller.buscar_cliente(id_cliente=id_cliente)
        mesa = self.mesa_controller.buscar_mesa(id_mesa)
        
        if not cliente:
            raise ValueError("Cliente no encontrado")
        if not mesa:
            raise ValueError("Mesa no encontrada")
        if mesa.estado != "disponible":
            raise ValueError("La mesa no está disponible")
        if mesa.capacidad < num_personas:
            raise ValueError("La mesa no tiene capacidad suficiente")
        
        reserva = Reserva(self.next_id, cliente, mesa, fecha, hora, num_personas)
        mesa.ocupar()
        cliente.agregar_reserva(reserva)
        self.reservas.append(reserva)
        self.next_id += 1
        
        # Enviar email de confirmación
        enviar_email_confirmacion(cliente, reserva)
        
        return reserva

    def modificar_reserva(self, id_reserva, nueva_mesa=None, nueva_fecha=None, nueva_hora=None, nuevo_num_personas=None):
        reserva = self.buscar_reserva(id_reserva)
        if not reserva:
            raise ValueError("Reserva no encontrada")
        
        # Verificar nueva mesa si se proporciona
        if nueva_mesa:
            mesa = self.mesa_controller.buscar_mesa(nueva_mesa)
            if not mesa or mesa.estado != "disponible":
                raise ValueError("La nueva mesa no está disponible")
        
        reserva.modificar(
            nueva_mesa=mesa if nueva_mesa else None,
            nueva_fecha=nueva_fecha,
            nueva_hora=nueva_hora,
            nuevo_num_personas=nuevo_num_personas
        )
        
        # Enviar email de confirmación con los cambios
        enviar_email_confirmacion(reserva.cliente, reserva)
        
        return reserva

    def cancelar_reserva(self, id_reserva):
        reserva = self.buscar_reserva(id_reserva)
        if reserva:
            reserva.cancelar()
            # Enviar email de cancelación
            enviar_email_confirmacion(reserva.cliente, reserva, cancelada=True)
            return True
        return False

    def buscar_reserva(self, id_reserva):
        for reserva in self.reservas:
            if reserva.id_reserva == id_reserva:
                return reserva
        return None

    def reservas_por_fecha(self, fecha):
        return [reserva for reserva in self.reservas if reserva.fecha == fecha and reserva.estado == "confirmada"]