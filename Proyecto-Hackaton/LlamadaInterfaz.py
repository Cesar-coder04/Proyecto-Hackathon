import sys

from PySide6.QtWidgets import QWidget,QMainWindow, QApplication, QMessageBox, QLineEdit
# from interfaz_ui import Ui_MainWindow
from vistas.interfaz_ui import Ui_MainWindow

# from recursos.LetrasEstaticas import letras_estaticas
from vistas.llamada_ui import Ui_MainWindow
class MiApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

 

   
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = MiApp() 
    mi_app.show()
    app.exec()
