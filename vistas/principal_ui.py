# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'principal.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)
import tkinter


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        MainWindow.resize(800,600)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setBaseSize(800,600)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_logo = QLabel(self.centralwidget)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setGeometry(QRect(150, 0, 491, 392))
        self.label_logo.setPixmap(QPixmap(u"traductor_de_gestos/images/logo.png"))
        self.pushButton_inciar = QPushButton(self.centralwidget)
        self.pushButton_inciar.setObjectName(u"pushButton_inciar")
        self.pushButton_inciar.setGeometry(QRect(200, 450, 91, 51))
        self.pushButton_inciar.setStyleSheet(u"background-color: rgb(97, 206, 228);\n"
"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.pushButton_cancelar = QPushButton(self.centralwidget)
        self.pushButton_cancelar.setObjectName(u"pushButton_cancelar")
        self.pushButton_cancelar.setGeometry(QRect(470, 450, 91, 51))
        self.pushButton_cancelar.setStyleSheet(u"background-color: rgb(253, 69, 77);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_logo.setText("")
        self.pushButton_inciar.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.pushButton_cancelar.setText(QCoreApplication.translate("MainWindow", u"Cerrar", None))
    # retranslateUi

