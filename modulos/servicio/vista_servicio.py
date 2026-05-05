from base.vista_popup import BasePopup
from .modelo_servicio import Servicio

class ServicioPopup(BasePopup):
    
    def abrir(self):
        super().abrir(title="Servicio")

