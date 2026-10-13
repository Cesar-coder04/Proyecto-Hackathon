# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'premium.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Planespremium(object):
    def setupUi(self, Planespremium):
        if not Planespremium.objectName():
            Planespremium.setObjectName(u"Planespremium")
        Planespremium.resize(1172, 649)
        Planespremium.setStyleSheet(u"background-color: rgb(30,30,30);")
        self.label_tarifas = QLabel(Planespremium)
        self.label_tarifas.setObjectName(u"label_tarifas")
        self.label_tarifas.setGeometry(QRect(0, 0, 1172, 571))
        self.label_tarifas.setPixmap(QPixmap(u"traductor_de_gestos\\images\\tarifas.png"))
        self.pushButton_pro = QPushButton(Planespremium)
        self.pushButton_pro.setObjectName(u"pushButton_pro")
        self.pushButton_pro.setGeometry(QRect(300, 563, 275, 45))
        self.pushButton_pro.setStyleSheet(u"font: 600 22pt \"Goudy Old Style\";\n"
"background-color: rgb(94, 94, 94);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_pro.setIconSize(QSize(30, 30))
        self.pushButton_enterprise = QPushButton(Planespremium)
        self.pushButton_enterprise.setObjectName(u"pushButton_enterprise")
        self.pushButton_enterprise.setGeometry(QRect(585, 563, 275, 45))
        self.pushButton_enterprise.setStyleSheet(u"font: 600 22pt \"Goudy Old Style\";\n"
"background-color: rgb(94, 94, 94);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_enterprise.setIconSize(QSize(30, 30))
        self.pushButton_enterprise_pro = QPushButton(Planespremium)
        self.pushButton_enterprise_pro.setObjectName(u"pushButton_enterprise_pro")
        self.pushButton_enterprise_pro.setGeometry(QRect(868, 563, 285, 45))
        self.pushButton_enterprise_pro.setStyleSheet(u"font: 600 22pt \"Goudy Old Style\";\n"
"background-color: rgb(94, 94, 94);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_enterprise_pro.setIconSize(QSize(30, 30))

        self.retranslateUi(Planespremium)

        QMetaObject.connectSlotsByName(Planespremium)
    # setupUi

    def retranslateUi(self, Planespremium):
        Planespremium.setWindowTitle(QCoreApplication.translate("Planespremium", u"Planes Premium", None))
        self.label_tarifas.setText("")
        self.pushButton_pro.setText(QCoreApplication.translate("Planespremium", u"AMPLIAR PLAN", None))
        self.pushButton_enterprise.setText(QCoreApplication.translate("Planespremium", u"AMPLIAR PLAN", None))
        self.pushButton_enterprise_pro.setText(QCoreApplication.translate("Planespremium", u"AMPLIAR PLAN", None))
    # retranslateUi

