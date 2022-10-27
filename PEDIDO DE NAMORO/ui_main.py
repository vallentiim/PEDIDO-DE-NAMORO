# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainFKAEjT.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget)
import resource_rc
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 438)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(161, 12, 7, 255));\n"
"}\n"
"\n"
"QLabel#Pergunta{\n"
"	font-size: 18px;\n"
"	font-weight: bold;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton{\n"
"	font-size: 20px;\n"
"	color: red;\n"
"	min-height: 45px;\n"
"	border-radius: 15px;\n"
"	background-color: white;\n"
"}")
        self.Pergunta = QLabel(self.centralwidget)
        self.Pergunta.setObjectName(u"Pergunta")
        self.Pergunta.setGeometry(QRect(-10, 0, 471, 61))
        self.Pergunta.setAlignment(Qt.AlignCenter)
        self.frame_yes = QFrame(self.centralwidget)
        self.frame_yes.setObjectName(u"frame_yes")
        self.frame_yes.setGeometry(QRect(60, 190, 95, 61))
        self.frame_yes.setFrameShape(QFrame.NoFrame)
        self.frame_yes.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_yes)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.button_yes = QPushButton(self.frame_yes)
        self.button_yes.setObjectName(u"button_yes")

        self.horizontalLayout_2.addWidget(self.button_yes)

        self.frame_no = QFrame(self.centralwidget)
        self.frame_no.setObjectName(u"frame_no")
        self.frame_no.setGeometry(QRect(300, 190, 95, 61))
        self.frame_no.setFrameShape(QFrame.NoFrame)
        self.frame_no.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_no)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_no = QPushButton(self.frame_no)
        self.button_no.setObjectName(u"button_no")

        self.horizontalLayout.addWidget(self.button_no)

        self.coracao = QLabel(self.centralwidget)
        self.coracao.setObjectName(u"coracao")
        self.coracao.setGeometry(QRect(80, 60, 301, 301))
        self.coracao.setPixmap(QPixmap(u":/images/coracao.png"))
        self.coracao.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Pergunta.setText(QCoreApplication.translate("MainWindow", u"OI, VOC\u00ca ACEITA VOLTAR A SER O LOVE DE KLEKLE?", None))
        self.button_yes.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.button_no.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.coracao.setText("")
    # retranslateUi

