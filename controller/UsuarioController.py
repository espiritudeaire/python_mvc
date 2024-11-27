from PyQt6.QtWidgets import QApplication
from view.ventana_principal import VentanaPrincipal
import sys

class UsuarioController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        
        self.vista.signal_login.connect(self.procesar_login)
    
    def procesar_login(self, username, passw):
        if self.modelo.validar_usuario(username, passw):
            #self.vista.mostrar_mensaje("LOGIN EXITOSO", "Inicio de sesión correcto")
            self.main_window = VentanaPrincipal(username)
            self.main_window.show()
            self.vista.close()
            
        else:
            self.vista.mostrar_mensaje("ERROR", "Usuario o contraseña incorrectos.")
            return False
    