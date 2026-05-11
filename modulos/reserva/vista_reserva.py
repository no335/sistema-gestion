from base.vista_popup import BasePopup
from .modelo_reserva import Reserva

class ReservaPopup(BasePopup):
    
    def abrir(self):
        super().abrir(title="Venta")
