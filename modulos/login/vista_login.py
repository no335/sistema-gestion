from base.vista_popup import BasePopup

class LoginPopup(BasePopup):
    
    def abrir(self):
        super().abrir(title="Login")
