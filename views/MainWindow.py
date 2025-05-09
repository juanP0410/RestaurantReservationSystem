import tkinter as tk
from tkinter import ttk
from controllers import ClienteController, MesaController, ReservaController

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Reservas - Administración")
        self.geometry("1000x600")
        
        # Inicializar controladores
        self.cliente_controller = ClienteController()
        self.mesa_controller = MesaController()
        self.reserva_controller = ReservaController(
            self.cliente_controller, 
            self.mesa_controller
        )
        
        # Crear algunas mesas de ejemplo
        for cap in [2, 2, 4, 4, 6, 8]:
            self.mesa_controller.agregar_mesa(cap)
        
        # Configurar la interfaz
        self._configurar_interfaz()
    
    def _configurar_interfaz(self):
        # Notebook (pestañas)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Pestaña de Clientes
        self.tab_clientes = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_clientes, text="Clientes")
        self._configurar_tab_clientes()
        
        # Pestaña de Mesas
        self.tab_mesas = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_mesas, text="Mesas")
        self._configurar_tab_mesas()
        
        # Pestaña de Reservas
        self.tab_reservas = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_reservas, text="Reservas")
        self._configurar_tab_reservas()
        
        # Pestaña de Disponibilidad
        self.tab_disponibilidad = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_disponibilidad, text="Disponibilidad")
        self._configurar_tab_disponibilidad()
    
    def _configurar_tab_clientes(self):
        # Implementar interfaz para gestión de clientes
        pass
    
    def _configurar_tab_mesas(self):
        # Implementar interfaz para gestión de mesas
        pass
    
    def _configurar_tab_reservas(self):
        # Implementar interfaz para gestión de reservas
        pass
    
    def _configurar_tab_disponibilidad(self):
        # Implementar interfaz para consulta de disponibilidad
        pass

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()