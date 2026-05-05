from base.vista_popup import BasePopup
from .modelo_usuario import Usuario

class LoginPopup(BasePopup):
    
    def abrir(self):
        super().abrir(title="Login")
