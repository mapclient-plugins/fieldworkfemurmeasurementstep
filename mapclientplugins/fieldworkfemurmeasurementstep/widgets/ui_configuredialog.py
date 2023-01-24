# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        if not ConfigureDialog.objectName():
            ConfigureDialog.setObjectName(u"ConfigureDialog")
        ConfigureDialog.resize(593, 178)
        self.verticalLayout_2 = QVBoxLayout(ConfigureDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(ConfigureDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.identifierLineEdit = QLineEdit(self.groupBox)
        self.identifierLineEdit.setObjectName(u"identifierLineEdit")

        self.gridLayout.addWidget(self.identifierLineEdit, 0, 1, 1, 1)

        self.identifierLabel = QLabel(self.groupBox)
        self.identifierLabel.setObjectName(u"identifierLabel")

        self.gridLayout.addWidget(self.identifierLabel, 0, 0, 1, 1)

        self.verboseLabel = QLabel(self.groupBox)
        self.verboseLabel.setObjectName(u"verboseLabel")
        self.verboseLabel.setMinimumSize(QSize(71, 0))

        self.gridLayout.addWidget(self.verboseLabel, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.verboseCheckBox = QCheckBox(self.groupBox)
        self.verboseCheckBox.setObjectName(u"verboseCheckBox")

        self.gridLayout.addWidget(self.verboseCheckBox, 1, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.buttonBox = QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.identifierLabel.setBuddy(self.identifierLineEdit)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(ConfigureDialog)
        self.buttonBox.accepted.connect(ConfigureDialog.accept)
        self.buttonBox.rejected.connect(ConfigureDialog.reject)

        QMetaObject.connectSlotsByName(ConfigureDialog)
    # setupUi

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QCoreApplication.translate("ConfigureDialog", u"Configure - Zinc Model Source", None))
        self.groupBox.setTitle("")
        self.identifierLabel.setText(QCoreApplication.translate("ConfigureDialog", u"Identifier:", None))
        self.verboseLabel.setText(QCoreApplication.translate("ConfigureDialog", u"Verbose:", None))
        self.verboseCheckBox.setText("")
    # retranslateUi

