import sys

from PySide6.QtWidgets import QWidget,QMainWindow, QApplication, QMessageBox, QLineEdit
from vistas.principal_ui import Ui_MainWindow
from controladores.ventana_seleccion import VSeleccion

import numpy as np
import cv2
import mediapipe as mp


class MiApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_cancelar.clicked.connect(self.f_cerrar)
        self.pushButton_inciar.clicked.connect(self.f_abrirseleccion)

    def f_cerrar(self):
        self.close()
    def f_abrirseleccion(self):
        self.ventana = VSeleccion(self)
        self.ventana.show()
    def f_reabrir(self):
        self.show()  
        
        
        


   
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = MiApp() 
    mi_app.show()
    app.exec()
