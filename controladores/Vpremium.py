from PySide6.QtWidgets import QWidget,QMessageBox

from vistas.premium_ui import Ui_Planespremium

class Vpremium(QWidget, Ui_Planespremium):
    def __init__(self): 
        super().__init__()
        self.setupUi(self)