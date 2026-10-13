# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prueba.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,QTimer)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QLCDNumber, QLabel, QMainWindow, QSizePolicy,
    QWidget)
import cv2
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1111, 800)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(237, 250, 239);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 40, 761, 661))
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        # Camara
        self.disp_main = QLabel(self.groupBox)
        self.disp_main.setObjectName(u"disp_main")
        self.disp_main.setMaximumSize(QSize(511, 258))
        self.disp_main.setStyleSheet(u"background-color: rgb(246, 247, 247);")
        self.disp_main.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cap=cv2.VideoCapture(0)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.f_camara)
        self.timer.start(30)



        self.gridLayout_3.addWidget(self.disp_main, 0, 0, 1, 1)

       
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Object Counting Software", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Main", None))
        self.disp_main.setText(QCoreApplication.translate("MainWindow", u"Main Source", None))
    # retranslateUi

    def f_camara(self):
        ret, frame = self.cap.read()
        if ret:
            # Convierte el frame de BGR a RGB
            rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            rgbImage =  cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
            rgbImage=cv2.set
            # Crea una imagen QImage a partir del frame
            h, w, ch = rgbImage.shape
            qImg = QImage(rgbImage.data, w, h, ch * w, QImage.Format_RGB888)
            # Crea un QPixmap a partir de la imagen QImage
            pixmap = QPixmap.fromImage(qImg)
            # Establece el QPixmap en el label
            self.disp_main.setPixmap(pixmap)
        