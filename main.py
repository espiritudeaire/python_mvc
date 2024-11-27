from view.login_view import Login 
from PyQt6.QtWidgets import QApplication, QWidget
import sys, numpy as np
from model.Usuario import Usuario
from controller.UsuarioController import UsuarioController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    matriz_prueba = np.random.rand(8, 2000, 180)  # Datos de ejemplo
    
    
    
    vista = Login()
    modelo = Usuario()
    controlador = UsuarioController(modelo, vista)
    
    
    
    
    
    sys.exit(app.exec())