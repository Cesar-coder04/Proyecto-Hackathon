# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'seleccion.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form_seleccion(object):
    def setupUi(self, Form_seleccion):
        if not Form_seleccion.objectName():
            Form_seleccion.setObjectName(u"Form_seleccion")
        Form_seleccion.resize(224, 206)
        Form_seleccion.setStyleSheet(u"background-color: rgb(44, 44, 44);")
        self.comboBox_opciones = QComboBox(Form_seleccion)
        self.comboBox_opciones.addItem("")
        self.comboBox_opciones.addItem("")
        self.comboBox_opciones.addItem("")
        self.comboBox_opciones.setObjectName(u"comboBox_opciones")
        self.comboBox_opciones.setGeometry(QRect(30, 80, 161, 41))
        self.comboBox_opciones.setStyleSheet(u"background-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255);")
        self.comboBox_opciones.setEditable(True)
        self.pushButton_aceptar = QPushButton(Form_seleccion)
        self.pushButton_aceptar.setObjectName(u"pushButton_aceptar")
        self.pushButton_aceptar.setGeometry(QRect(20, 160, 75, 24))
        self.pushButton_aceptar.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_cancelar = QPushButton(Form_seleccion)
        self.pushButton_cancelar.setObjectName(u"pushButton_cancelar")
        self.pushButton_cancelar.setGeometry(QRect(130, 160, 75, 24))
        self.pushButton_cancelar.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_tipo = QLabel(Form_seleccion)
        self.label_tipo.setObjectName(u"label_tipo")
        self.label_tipo.setGeometry(QRect(30, 10, 181, 51))
        self.label_tipo.setStyleSheet(u"background-color: rgb(44, 44, 44);\n"
"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.retranslateUi(Form_seleccion)

        QMetaObject.connectSlotsByName(Form_seleccion)
    # setupUi

    def retranslateUi(self, Form_seleccion):
        Form_seleccion.setWindowTitle(QCoreApplication.translate("Form_seleccion", u"Form", None))
        self.comboBox_opciones.setItemText(0, QCoreApplication.translate("Form_seleccion", u"Est\u00e1ndar", None))
        self.comboBox_opciones.setItemText(1, QCoreApplication.translate("Form_seleccion", u"Voz a texto", None))
        self.comboBox_opciones.setItemText(2, QCoreApplication.translate("Form_seleccion", u"Traducci\u00f3n de gestos", None))

        self.comboBox_opciones.setCurrentText(QCoreApplication.translate("Form_seleccion", u"Est\u00e1ndar", None))
        self.comboBox_opciones.setPlaceholderText("")
        self.pushButton_aceptar.setText(QCoreApplication.translate("Form_seleccion", u"Aceptar", None))
        self.pushButton_cancelar.setText(QCoreApplication.translate("Form_seleccion", u"Cancelar", None))
        self.label_tipo.setText(QCoreApplication.translate("Form_seleccion", u"Selecciona el tipo de servicio", None))
    # retranslateUi

