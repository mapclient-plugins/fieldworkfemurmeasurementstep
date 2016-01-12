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
import json

from PySide import QtGui

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint

from mapclientplugins.fieldworkfemurmeasurementstep.widgets.configuredialog import ConfigureDialog
from gias.musculoskeletal import fw_femur_measurements
from fieldwork.field import geometric_field

class FieldworkFemurMeasurementStep(WorkflowStepMountPoint):
    '''
    Take morphometric measurements on a fieldwork femur mesh
    '''
    
    def __init__(self, location):
        super(FieldworkFemurMeasurementStep, self).__init__('Fieldwork Femur Measurements', location)
        self._category = 'Anthropometry'
        # self._icon = QtGui.QImage(':/zincmodelsource/images/zinc_model_icon.png')   # change this
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'ju#fieldworkmodel'))
        # self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port', 'http://physiomeproject.org/workflow/1.0/rdf-schema#provides', 'ju#fieldworkfemurmeasurement'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'ju#fieldworkmeasurementdict'))

        self._widget = None
        self.measurements = None
        self.model = None
        self._config = {}
        self._config['identifier'] = ''
        self._config['verbose'] = True

    def configure(self):

        dlg = ConfigureDialog()
        dlg.identifierOccursCount = self._identifierOccursCount
        dlg.setConfig(self._config)
        dlg.validate()
        dlg.setModal(True)
        
        if dlg.exec_():
            self._config = dlg.getConfig()
        
        self._configured = dlg.validate()
        self._configuredObserver()

    def execute(self):

        self.measurements = fw_femur_measurements.FemurMeasurements( self.model )
        self.measurements.calcMeasurements()
        
        if self._config['verbose']:
            self.measurements.printMeasurements()
            
        # return m
        print('measurements done')
        self._doneExecution()

    def setPortData(self, index, dataIn):
        if not isinstance(dataIn, geometric_field.geometric_field):
            raise TypeError('FieldViViewFieldworkModelStep expects a geometric_field as input')
        
        self.model = dataIn

    def getPortData(self, index):
        print('outputting from FieldworkFemurMeasurementStep')
        return {'femur measurements':self.measurements}
    
    def getIdentifier(self):
        return self._config['identifier']
     
    def setIdentifier(self, identifier):
        self._config['identifier'] = identifier
     
    def serialize(self):
        '''
        Add code to serialize this step to disk. Returns a json string for
        mapclient to serialise.
        '''
        return json.dumps(self._config, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def deserialize(self, string):
        '''
        Add code to deserialize this step from disk. Parses a json string
        given by mapclient
        '''
        self._config.update(json.loads(string))

        d = ConfigureDialog()
        d.identifierOccursCount = self._identifierOccursCount
        d.setConfig(self._config)
        self._configured = d.validate()

