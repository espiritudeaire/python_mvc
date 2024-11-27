import sys
from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, QLineEdit, QPushButton, QMessageBox, QCheckBox, QMainWindow, QVBoxLayout, QDialog)
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import pyqtSignal

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

class VentanaPrincipal(QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.inicializarUI()
    
    def inicializarUI(self):
        self.setWindowTitle("Ventana Principal")
        self.setGeometry(100,100,600,600)
        
        self.label = QLabel(f"¡Bienvenido, {self.username}!", self)
        
        self.update_button = QPushButton('Actualizar gráfica')
        self.update_button.clicked.connect(self.actualizar_grafica)
        
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.canvas)
        layout.addWidget(self.update_button)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        self.graficar_funcion()
        
    
    def graficar_funcion(self, pendiente=1, intercepto=0):
        ax = self.figure.add_subplot(111)
        ax.clear()
        
        x = np.linspace(-10, 10, 100)
        y = pendiente * x + intercepto
        
        ax.plot(x, y, label=f'y = {pendiente}x + {intercepto}')
        ax.set_title("Gráfica de una función lineal")
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.legend()
        
        self.canvas.draw()
        
    def actualizar_grafica(self):
        nueva_pendiente = np.random.uniform(-5, 5)
        nuevo_intercepto = np.random.uniform(-10, 10)
        self.graficar_funcion(nueva_pendiente, nuevo_intercepto)