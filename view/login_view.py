import sys
from PyQt6.QtWidgets import (QApplication,
                             QLabel, QWidget, QLineEdit,
                             QPushButton, QMessageBox, QCheckBox,
                             QMainWindow, QVBoxLayout)
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import pyqtSignal

class Login(QMainWindow):
    signal_login = pyqtSignal(str, str)
    
    def __init__(self):
        super().__init__()
        self.inicializarUI()
    
    def inicializarUI(self):
        self.setWindowTitle("Inició de Sesión")
        self.setGeometry(500, 500, 350,100)
        self.generar_formulario()
        self.show()
    
    def generar_formulario(self):
        self.is_logged = False
        self.widget = QWidget()
        self.layout = QVBoxLayout()
        
        # campo usuario        
        self.user_label = QLabel(self)
        self.user_label.setText("Usuario:")
        self.user_label.setFont(QFont('Arial', 10))
        self.layout.addWidget(self.user_label)
        
        self.user_input = QLineEdit(self)
        self.layout.addWidget(self.user_input)
        
        # campo contraseña
        self.pass_label = QLabel(self)
        self.pass_label.setText("Contraseña:")
        self.pass_label.setFont(QFont('Arial', 10))
        self.layout.addWidget(self.pass_label)
        
        self.pass_input = QLineEdit(self)
        self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.layout.addWidget(self.pass_input)

        #botones
        self.boton_login = QPushButton("Iniciar Sesión")
        self.layout.addWidget(self.boton_login)
        
        self.boton_registrar = QPushButton("Registrarse")
        self.layout.addWidget(self.boton_registrar)
        
        # 
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        
        self.boton_login.clicked.connect(self.enviar_login)
    
    def enviar_login(self):
        username = self.user_input.text()
        passw = self.pass_input.text()
        login = self.signal_login.emit(username, passw)
        print(login)
    
    def mostrar_mensaje(self, titulo, mensaje):
        msg = QMessageBox(self)
        msg.setWindowTitle(titulo)
        msg.setText(mensaje)
        msg.exec()
        
    