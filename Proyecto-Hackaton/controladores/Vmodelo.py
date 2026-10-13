from PySide6.QtWidgets import QWidget,QMessageBox

from controladores.Vpremium import Vpremium
from vistas.llamada_ui import Ui_MainWindow


class VModelo(QWidget, Ui_MainWindow):
    def __init__(self,ventanainicial): 
        super().__init__()
        self.setupUi(self)
        self.historial = historial = []
        self.ventanainicial = ventanainicial
        self.pushButton_casa.clicked.connect(self.F_casa)
        self.pushButton_colgar.clicked.connect(self.F_colgar)
        self.pushButton_enviar.clicked.connect(self.F_enviar)
        self.pushButton_premium.clicked.connect(self.F_premium)
    def F_casa(self):
        self.close()
        self.ventanainicial.f_reabrir()
    def F_colgar(self):
        self.close()
        
    def F_enviar(self):

        mensaje =self.lineEdit.text()
        if (mensaje.isspace()==False and mensaje != ""):
            
            self.historial.append(mensaje)
            self.textBrowser_historial.clear()
            for i in self.historial:
                
                self.textBrowser_historial.insertPlainText(f'-{i}\n')
        self.lineEdit.clear()
        
    def F_premium(self):
        self.ventanapremium = Vpremium()
        self.ventanapremium.show()



        