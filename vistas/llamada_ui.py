# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'llamada.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import cv2
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTimer, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QSizePolicy,
                               QTextBrowser, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(862, 689)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(26, 26, 26);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(70, 20, 761, 661))
        self.disp_main = QLabel(self.groupBox)


        self.disp_main.setObjectName(u"disp_main")     
        self.disp_main.setGeometry(QRect(30, 40, 281, 258))
        self.disp_main.setMaximumSize(QSize(511, 258))
        self.disp_main.setStyleSheet(u"background-color: rgb(246, 247, 247);")
        self.disp_main.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.cap = cv2.VideoCapture(0)  # Abre la cámara predeterminada
        self.timer = QTimer()
        self.timer.timeout.connect(self.f_camara)
        self.timer.start(30)

        
        self.disp_recibe = QLabel(self.groupBox)
        self.disp_recibe.setObjectName(u"disp_recibe")
        self.disp_recibe.setGeometry(QRect(440, 40, 281, 258))
        self.disp_recibe.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_apagarcamara = QPushButton(self.groupBox)
        self.pushButton_apagarcamara.setObjectName(u"pushButton_apagarcamara")
        self.pushButton_apagarcamara.setGeometry(QRect(360, 330, 40, 40))
        self.pushButton_apagarcamara.setStyleSheet(u"QPushButton {\n"
"   \n"
"    border: 2px solid #0d7fd1;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #0d7fd1\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        icon = QIcon()
        icon.addFile(u"traductor_de_gestos/images/ojo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_apagarcamara.setIcon(icon)
        self.pushButton_apagarcamara.setIconSize(QSize(25, 25))
        self.pushButton_activardeteccion = QPushButton(self.groupBox)
        self.pushButton_activardeteccion.setObjectName(u"pushButton_activardeteccion")
        self.pushButton_activardeteccion.setGeometry(QRect(420, 330, 40, 40))
        self.pushButton_activardeteccion.setStyleSheet(u"QPushButton {\n"
"    background-color: #cc0606;\n"
"    border: 2px solid #0aad1d;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #0aad1d\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        icon1 = QIcon()
        icon1.addFile(u"traductor_de_gestos/images/iniciar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_activardeteccion.setIcon(icon1)
        self.pushButton_activardeteccion.setIconSize(QSize(25, 25))
        self.pushButton_colgar = QPushButton(self.groupBox)
        self.pushButton_colgar.setObjectName(u"pushButton_colgar")
        self.pushButton_colgar.setGeometry(QRect(300, 330, 40, 40))
        self.pushButton_colgar.setStyleSheet(u"QPushButton {\n"
"    background-color: #cc0606;\n"
"    border: 2px solid #8a0606;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #8a0606\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        icon2 = QIcon()
        icon2.addFile(u"traductor_de_gestos/images/colgar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_colgar.setIcon(icon2)
        self.pushButton_colgar.setIconSize(QSize(25, 25))
        self.label_letras = QLabel(self.groupBox)
        self.label_letras.setObjectName(u"label_letras")
        self.label_letras.setGeometry(QRect(50, 360, 201, 161))
        self.label_letras.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.pushButton_enviar = QPushButton(self.groupBox)
        self.pushButton_enviar.setObjectName(u"pushButton_enviar")
        self.pushButton_enviar.setGeometry(QRect(630, 575, 40, 40))
        self.pushButton_enviar.setStyleSheet(u"background-color: rgb(97, 97, 97);")
        icon3 = QIcon()
        icon3.addFile(u"traductor_de_gestos/images/enviar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_enviar.setIcon(icon3)
        self.pushButton_enviar.setIconSize(QSize(30, 20))
        self.pushButton_adjuntar = QPushButton(self.groupBox)
        self.pushButton_adjuntar.setObjectName(u"pushButton_adjuntar")
        self.pushButton_adjuntar.setGeometry(QRect(590, 575, 40, 40))
        self.pushButton_adjuntar.setStyleSheet(u"background-color: rgb(94, 94, 94);")
        icon4 = QIcon()
        icon4.addFile(u"traductor_de_gestos/images/adjuntar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_adjuntar.setIcon(icon4)
        self.pushButton_adjuntar.setIconSize(QSize(35, 35))
        self.label_chat = QLabel(self.groupBox)
        self.label_chat.setObjectName(u"label_chat")
        self.label_chat.setGeometry(QRect(60, 570, 621, 51))
        self.label_chat.setStyleSheet(u"background-color: rgb(94, 94, 94);")
        self.pushButton_adjuntar_2 = QPushButton(self.groupBox)
        self.pushButton_adjuntar_2.setObjectName(u"pushButton_adjuntar_2")
        self.pushButton_adjuntar_2.setGeometry(QRect(70, 575, 40, 40))
        self.pushButton_adjuntar_2.setStyleSheet(u"background-color: rgb(94, 94, 94);")
        icon5 = QIcon()
        icon5.addFile(u"traductor_de_gestos/images/bocadillo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_adjuntar_2.setIcon(icon5)
        self.pushButton_adjuntar_2.setIconSize(QSize(30, 35))
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(120, 575, 461, 41))
        self.lineEdit.setStyleSheet(u"background-color: rgb(94, 94, 94);")
        self.textBrowser_historial = QTextBrowser(self.groupBox)
        self.textBrowser_historial.setObjectName(u"textBrowser_historial")
        self.textBrowser_historial.setGeometry(QRect(470, 360, 201, 161))
        self.disp_main.raise_()
        self.disp_recibe.raise_()
        self.pushButton_apagarcamara.raise_()
        self.pushButton_activardeteccion.raise_()
        self.pushButton_colgar.raise_()
        self.label_letras.raise_()
        self.label_chat.raise_()
        self.pushButton_enviar.raise_()
        self.pushButton_adjuntar.raise_()
        self.pushButton_adjuntar_2.raise_()
        self.lineEdit.raise_()
        self.textBrowser_historial.raise_()
        self.pushButton_casa = QPushButton(self.centralwidget)
        self.pushButton_casa.setObjectName(u"pushButton_casa")
        self.pushButton_casa.setGeometry(QRect(20, 40, 40, 40))
        self.pushButton_casa.setStyleSheet(u"QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        icon6 = QIcon()
        icon6.addFile(u"traductor_de_gestos/images/casa.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_casa.setIcon(icon6)
        self.pushButton_casa.setIconSize(QSize(25, 25))
        self.pushButton_premium = QPushButton(self.centralwidget)
        self.pushButton_premium.setObjectName(u"pushButton_premium")
        self.pushButton_premium.setGeometry(QRect(20, 100, 40, 40))
        self.pushButton_premium.setStyleSheet(u"QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        icon7 = QIcon()
        icon7.addFile(u"traductor_de_gestos/images/premium.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_premium.setIcon(icon7)
        self.pushButton_premium.setIconSize(QSize(25, 25))
        self.pushButton_agregar = QPushButton(self.centralwidget)
        self.pushButton_agregar.setObjectName(u"pushButton_agregar")
        self.pushButton_agregar.setGeometry(QRect(20, 160, 40, 40))
        self.pushButton_agregar.setStyleSheet(u"QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        icon8 = QIcon()
        icon8.addFile(u"traductor_de_gestos/images/a\u00f1adir.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_agregar.setIcon(icon8)
        self.pushButton_agregar.setIconSize(QSize(27, 30))
        self.pushButton_informacion = QPushButton(self.centralwidget)
        self.pushButton_informacion.setObjectName(u"pushButton_informacion")
        self.pushButton_informacion.setGeometry(QRect(20, 220, 40, 40))
        self.pushButton_informacion.setStyleSheet(u"QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        icon9 = QIcon()
        icon9.addFile(u"traductor_de_gestos/images/info.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_informacion.setIcon(icon9)
        self.pushButton_informacion.setIconSize(QSize(30, 30))
        self.pushButton_configuracion = QPushButton(self.centralwidget)
        self.pushButton_configuracion.setObjectName(u"pushButton_configuracion")
        self.pushButton_configuracion.setGeometry(QRect(20, 610, 40, 40))
        self.pushButton_configuracion.setStyleSheet(u"QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        icon10 = QIcon()
        icon10.addFile(u"traductor_de_gestos/images/config.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_configuracion.setIcon(icon10)
        self.pushButton_configuracion.setIconSize(QSize(30, 30))
        # MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Object Counting Software", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Main", None))
        self.disp_main.setText(QCoreApplication.translate("MainWindow", u"Main Source", None))
        self.disp_recibe.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.pushButton_apagarcamara.setText("")
        self.pushButton_activardeteccion.setText("")
        self.pushButton_colgar.setText("")
        self.label_letras.setText("")
        self.pushButton_enviar.setText("")
        self.pushButton_adjuntar.setText("")
        self.label_chat.setText("")
        self.pushButton_adjuntar_2.setText("")
        self.pushButton_casa.setText("")
        self.pushButton_premium.setText("")
        self.pushButton_agregar.setText("")
        self.pushButton_informacion.setText("")
        self.pushButton_configuracion.setText("")
    # retranslateUi
    def f_camara(self):
        ret, rgbImage = self.cap.read()
        if ret:
                # Convierte el frame de BGR a RGB
                rgbImage = cv2.cvtColor(cv2.flip( rgbImage, 1),cv2.COLOR_BGR2RGB)

                # Crea una imagen QImage a partir del frame
                h, w, ch = rgbImage.shape
                qImg = QImage(rgbImage.data, w, h, ch * w, QImage.Format_RGB888)
                # Crea un QPixmap a partir de la imagen QImage
                pixmap = QPixmap.fromImage(qImg)
                # Establece el QPixmap en el label
                self.disp_main.setPixmap(pixmap)

