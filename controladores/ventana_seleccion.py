from PySide6.QtWidgets import QWidget,QMessageBox


from vistas.seleccion_ui import Ui_Form_seleccion


from controladores.Vmodelo import VModelo

class VSeleccion(QWidget, Ui_Form_seleccion):
    def __init__(self,ventanainicial): 
        super().__init__()
        self.setupUi(self)
        self.ventanainicial=ventanainicial
        self.pushButton_aceptar.clicked.connect(self.F_iniciarmain)
        self.pushButton_cancelar.clicked.connect(self.F_cerrarventana)
    def F_cerrarventana(self):
        self.close()

    def F_iniciarmain(self):
        self.ventana_main = VModelo(self.ventanainicial)
        self.ventana_main.show()
        self.ventanainicial.close()
        self.close()


        
        
       
        