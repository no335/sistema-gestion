from base.vista_popup import BasePopup
from .modelo_compra import Compra

class CompraPopup(BasePopup):

    def abrir(self):
        super().abrir(title="Compra")
