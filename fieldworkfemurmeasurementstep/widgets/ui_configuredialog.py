# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configuredialog.ui'
#
# Created: Wed Oct  2 17:40:46 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        ConfigureDialog.setObjectName("ConfigureDialog")
        ConfigureDialog.resize(593, 178)
        self.verticalLayout_2 = QtGui.QVBoxLayout(ConfigureDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtGui.QGroupBox(ConfigureDialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.identifierLineEdit = QtGui.QLineEdit(self.groupBox)
        self.identifierLineEdit.setObjectName("identifierLineEdit")
        self.gridLayout.addWidget(self.identifierLineEdit, 0, 1, 1, 1)
        self.identifierLabel = QtGui.QLabel(self.groupBox)
        self.identifierLabel.setObjectName("identifierLabel")
        self.gridLayout.addWidget(self.identifierLabel, 0, 0, 1, 1)
        self.verboseLabel = QtGui.QLabel(self.groupBox)
        self.verboseLabel.setMinimumSize(QtCore.QSize(71, 0))
        self.verboseLabel.setObjectName("verboseLabel")
        self.gridLayout.addWidget(self.verboseLabel, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.verboseCheckBox = QtGui.QCheckBox(self.groupBox)
        self.verboseCheckBox.setText("")
        self.verboseCheckBox.setObjectName("verboseCheckBox")
        self.gridLayout.addWidget(self.verboseCheckBox, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.identifierLabel.setBuddy(self.identifierLineEdit)

        self.retranslateUi(ConfigureDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ConfigureDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ConfigureDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ConfigureDialog)

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QtGui.QApplication.translate("ConfigureDialog", "Configure - Femur Measurement", None, QtGui.QApplication.UnicodeUTF8))
        self.identifierLabel.setText(QtGui.QApplication.translate("ConfigureDialog", "Identifier:", None, QtGui.QApplication.UnicodeUTF8))
        self.verboseLabel.setText(QtGui.QApplication.translate("ConfigureDialog", "Verbose:", None, QtGui.QApplication.UnicodeUTF8))

