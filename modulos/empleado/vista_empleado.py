from base.vista_popup import BasePopup
from .empleado_modelo import Empleado

class EmpleadoPopup(BasePopup):
    
    def abrir(self):
        super().abrir(title="Empleado")

