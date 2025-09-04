# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_tasks.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QListView, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(540, 415)
        MainWindow.setStyleSheet(u"background-color: rgb(61, 84, 93)\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 20, 400, 71))
        self.lineEdit.setStyleSheet(u"border-radius: 5%;\n"
"background-color: rgba(59, 59, 59, 0.5);\n"
"")
        self.postButton = QPushButton(self.centralwidget)
        self.postButton.setObjectName(u"postButton")
        self.postButton.setGeometry(QRect(430, 20, 91, 31))
        self.postButton.setStyleSheet(u"border-radius: 5%;\n"
"background-color: rgba(59, 59, 59, 0.5);")
        self.getButton = QPushButton(self.centralwidget)
        self.getButton.setObjectName(u"getButton")
        self.getButton.setGeometry(QRect(430, 60, 91, 31))
        self.getButton.setStyleSheet(u"border-radius: 5%;\n"
"background-color: rgba(59, 59, 59, 0.5);")
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(20, 100, 500, 291))
        self.listView.setStyleSheet(u"border-radius: 5%;\n"
"background-color: rgba(59, 59, 59, 0.5);\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Test Tasks", None))
        self.lineEdit.setText("")
        self.postButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.getButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c", None))
    # retranslateUi

