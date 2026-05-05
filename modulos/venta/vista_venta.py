from base.vista_popup import BasePopup
from .modelo_venta import Venta

class VentaPopup(BasePopup):
    
    def abrir(self):
        super().abrir(title="Venta")
