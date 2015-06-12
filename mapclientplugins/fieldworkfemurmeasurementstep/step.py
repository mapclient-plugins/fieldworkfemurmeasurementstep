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
from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint

from mapclientplugins.fieldworkfemurmeasurementstep.widgets.configuredialog import ConfigureDialog
from mapclientplugins.fieldworkfemurmeasurementstep.fieldworkfemurmeasurementdata import StepState
from gias.musculoskeletal import fw_femur_measurements
from fieldwork.field import geometric_field

class FieldworkFemurMeasurementStep(WorkflowStepMountPoint):
    '''
    Take morphometric measurements on a fieldwork femur mesh
    '''
    
    def __init__(self, location):
        super(FieldworkFemurMeasurementStep, self).__init__('Fieldwork Femur Measurements', location)
        self._category = 'Fieldwork Measurements'
        self._state = StepState()
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

    def configure(self):
        d = ConfigureDialog(self._state)
        d.setModal(True)
        if d.exec_():
            self._state = d.getState()
            
        self._configured = d.validate()
        if self._configured and self._configuredObserver:
            self._configuredObserver()

    def execute(self):

        self.measurements = fw_femur_measurements.FemurMeasurements( self.model )
        self.measurements.calcMeasurements()
        
        # if self._state._verbose:
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
        return self._state._identifier
     
    def setIdentifier(self, identifier):
        self._state._identifier = identifier
     
    def serialize(self):
        '''
        Add code to serialize this step to string.  This method should
        implement the opposite of 'deserialize'.
        '''
        return self._state.serialize()
     
    def deserialize(self, string):
        '''
        Add code to deserialize this step from string.  This method should
        implement the opposite of 'serialize'.
        '''
        self._state.deserialize(string)

        d = ConfigureDialog(self._state)
        self._configured = d.validate()

