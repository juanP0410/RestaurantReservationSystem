# utils/EmailSender.py
def enviar_email_confirmacion(cliente, reserva, cancelada=False):
    # Esta es una implementación simulada que imprimiría el email en consola
    # En una implementación real usarías un servicio de email como SMTP
    
    if cancelada:
        asunto = "Cancelación de reserva"
        mensaje = f"""
        Estimado/a {cliente.nombre},
        
        Su reserva para el {reserva.fecha} a las {reserva.hora} 
        en nuestra mesa {reserva.mesa.id_mesa} ha sido cancelada.
        
        Esperamos servirle en otra ocasión.
        """
    else:
        asunto = "Confirmación de reserva"
        mensaje = f"""
        Estimado/a {cliente.nombre},
        
        Su reserva ha sido confirmada con los siguientes detalles:
        
        Fecha: {reserva.fecha}
        Hora: {reserva.hora}
        Número de personas: {reserva.num_personas}
        Mesa asignada: {reserva.mesa.id_mesa} (Capacidad: {reserva.mesa.capacidad})
        
        ¡Gracias por elegir nuestro restaurante!
        """
    
    print(f"Enviando email a {cliente.email}")
    print(f"Asunto: {asunto}")
    print(f"Mensaje: {mensaje}")