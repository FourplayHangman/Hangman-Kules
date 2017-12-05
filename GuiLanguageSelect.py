# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LanguageSelector.ui'
#
# Created: Fri Nov 24 20:06:40 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_LanguageSelector(object):
    def setupUi(self, LanguageSelector):
        LanguageSelector.setObjectName("LanguageSelector")
        LanguageSelector.resize(300, 100)
        self.centralwidget = QtGui.QWidget(LanguageSelector)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Fixed,
                                       QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.SetLanguage = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,
                                       QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.SetLanguage.sizePolicy().hasHeightForWidth())
        self.SetLanguage.setSizePolicy(sizePolicy)
        self.SetLanguage.setObjectName("SetLanguage")
        self.horizontalLayout.addWidget(self.SetLanguage)
        spacerItem1 = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Fixed,
                                        QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        LanguageSelector.setCentralWidget(self.centralwidget)

        self.retranslateUi(LanguageSelector)
        QtCore.QMetaObject.connectSlotsByName(LanguageSelector)

    def retranslateUi(self, LanguageSelector):
        LanguageSelector.setWindowTitle(
            QtGui.QApplication.translate("LanguageSelector", "MainWindow",
                                         None, QtGui.QApplication.UnicodeUTF8))
        self.SetLanguage.setText(
            QtGui.QApplication.translate("LanguageSelector", "OK", None,
                                         QtGui.QApplication.UnicodeUTF8))
