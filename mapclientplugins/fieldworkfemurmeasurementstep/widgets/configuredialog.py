'''
MAP Client, a program to generate detailed musculoskeletal models for OpenSim.
    Copyright (C) 2012  University of Auckland
    
This file is part of MAP Client. (http://launchpad.net/mapclient)

    MAP Client is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    MAP Client is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with MAP Client.  If not, see <http://www.gnu.org/licenses/>..
'''
import os

from PySide2.QtWidgets import QDialog, QDialogButtonBox

from mapclientplugins.fieldworkfemurmeasurementstep.widgets.ui_configuredialog import Ui_ConfigureDialog
from mapclientplugins.fieldworkfemurmeasurementstep.fieldworkfemurmeasurementdata import StepState

REQUIRED_STYLE_SHEET = 'border: 1px solid red; border-radius: 3px'
DEFAULT_STYLE_SHEET = ''


class ConfigureDialog(QDialog):
    '''
    Configure dialog to present the user with the options to configure this step.
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        QDialog.__init__(self, parent)
        
        self._ui = Ui_ConfigureDialog()
        self._ui.setupUi(self)

        # Keep track of the previous identifier so that we can track changes
        # and know how many occurrences of the current identifier there should
        # be.
        self._previousIdentifier = ''

        # Set a place holder for a callable that will get set from the step.
        # We will use this method to decide whether the identifier is unique.
        self.identifierOccursCount = None

        self._makeConnections()

    def _makeConnections(self):
        self._ui.identifierLineEdit.textChanged.connect(self.validate)

    def setConfig(self, config):
        self._previousIdentifier = config['identifier']
        self._ui.identifierLineEdit.setText(config['identifier'])
        self._ui.verboseCheckBox.setChecked(config['verbose'])

    def getConfig(self):
        '''
        Get the current value of the configuration from the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        '''
        self._previousIdentifier = self._ui.identifierLineEdit.text()
        config = {}
        config['identifier'] = self._ui.identifierLineEdit.text()
        config['verbose'] = self._ui.verboseCheckBox.isChecked()
        return config

    def validate(self):
        identifierValid = len(self._ui.identifierLineEdit.text()) > 0
        if identifierValid:
            self._ui.identifierLineEdit.setStyleSheet(DEFAULT_STYLE_SHEET)
        else:
            self._ui.identifierLineEdit.setStyleSheet(REQUIRED_STYLE_SHEET)

        valid = identifierValid
        # self._ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(valid)

        return valid
