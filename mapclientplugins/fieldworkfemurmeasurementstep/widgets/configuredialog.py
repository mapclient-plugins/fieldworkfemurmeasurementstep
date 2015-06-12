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

from PySide.QtGui import QDialog, QFileDialog, QDialogButtonBox

from mapclientplugins.fieldworkfemurmeasurementstep.widgets.ui_configuredialog import Ui_ConfigureDialog
from mapclientplugins.fieldworkfemurmeasurementstep.fieldworkfemurmeasurementdata import StepState

REQUIRED_STYLE_SHEET = 'border: 1px solid red; border-radius: 3px'
DEFAULT_STYLE_SHEET = ''

class ConfigureDialog(QDialog):
    '''
    Configure dialog to present the user with the options to configure this step.
    '''

    def __init__(self, state, parent=None):
        '''
        Constructor
        '''
        QDialog.__init__(self, parent)
        self._ui = Ui_ConfigureDialog()
        self._ui.setupUi(self)
        
        self.setState(state)
        self.validate()
        self._makeConnections()
        
    def _makeConnections(self):
        self._ui.identifierLineEdit.textChanged.connect(self.validate)
      
    
    def setState(self, state):
        self._ui.identifierLineEdit.setText(state._identifier)
        self._ui.verboseCheckBox.setChecked(state._verbose)
    
    def getState(self):
        state = StepState()
        state._identifier = self._ui.identifierLineEdit.text()
        state._verbose = self._ui.verboseCheckBox.isChecked()
        
        return state
        
    def validate(self):
        identifierValid = len(self._ui.identifierLineEdit.text()) > 0
        if identifierValid:
            self._ui.identifierLineEdit.setStyleSheet(DEFAULT_STYLE_SHEET)
        else:
            self._ui.identifierLineEdit.setStyleSheet(REQUIRED_STYLE_SHEET)

        valid = identifierValid
        self._ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(valid)

        return valid

