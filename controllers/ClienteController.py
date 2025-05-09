# controllers/ClienteController.py
from models.Cliente import Cliente
from utils.Validators import validar_email_unico

class ClienteController:
    def __init__(self):
        self.clientes = []
        self.next_id = 1

    def registrar_cliente(self, nombre, email, telefono=None):
        if not validar_email_unico(email, self.clientes):
            raise ValueError("El correo electrónico ya está registrado")
        
        cliente = Cliente(self.next_id, nombre, email, telefono)
        self.clientes.append(cliente)
        self.next_id += 1
        return cliente

    def buscar_cliente(self, id_cliente=None, email=None):
        for cliente in self.clientes:
            if (id_cliente and cliente.id_cliente == id_cliente) or (email and cliente.email == email):
                return cliente
        return None

    def editar_cliente(self, id_cliente, nuevo_nombre=None, nuevo_email=None, nuevo_telefono=None):
        cliente = self.buscar_cliente(id_cliente=id_cliente)
        if not cliente:
            raise ValueError("Cliente no encontrado")
        
        if nuevo_email and nuevo_email != cliente.email:
            if not validar_email_unico(nuevo_email, self.clientes):
                raise ValueError("El nuevo correo electrónico ya está registrado")
            cliente.email = nuevo_email
        
        if nuevo_nombre:
            cliente.nombre = nuevo_nombre
        if nuevo_telefono:
            cliente.telefono = nuevo_telefono
        
        return cliente

    def eliminar_cliente(self, id_cliente):
        cliente = self.buscar_cliente(id_cliente=id_cliente)
        if cliente:
            self.clientes.remove(cliente)
            return True
        return False

    def obtener_historial_reservas(self, id_cliente):
        cliente = self.buscar_cliente(id_cliente=id_cliente)
        if cliente:
            return cliente.obtener_reservas()
        return []