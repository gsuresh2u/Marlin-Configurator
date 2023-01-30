
from Config import configfile

import configparser
config = configparser.ConfigParser(allow_no_value=True)
config.read(configfile)

#Read all Environments from text file
def read_environments():
    var1 = open("_environments.txt", "r").readlines()
    data = []
    for line in var1:
         data.append(line)
        #print(line)
    return data

#Read all Motherboards from text file
def read_boards():
    var1 = open("_boards.txt", "r").readlines()
    data = []
    for line in var1:
         data.append(line)
    return data

#Read all Drivers from text file
def read_drivers():
    var1 = open("_drivers.txt", "r").readlines()
    data = []
    for line in var1:
         data.append(line)
    return data




import sys 
from PyQt5 import QtCore, QtGui, QtWidgets, uic

class Conditions(QtWidgets.QDialog):
    def __init__(self):
        super(Conditions,self).__init__()
        uic.loadUi('Marlin.ui',self)

        self.X2_Driver.setEnabled(False)
        self.Y2_Driver.setEnabled(False)
        self.Z2_Driver.setEnabled(False)
        self.Z3_Driver.setEnabled(False)
        self.Z4_Driver.setEnabled(False)
        self.E1_Driver.setEnabled(False)
        self.E2_Driver.setEnabled(False)
        self.E2_Driver.setEnabled(False)
        self.E3_Driver.setEnabled(False)
        self.E4_Driver.setEnabled(False)
        self.E5_Driver.setEnabled(False)
        self.E6_Driver.setEnabled(False)
        self.E7_Driver.setEnabled(False)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  Start selection of X Driver comboboxes  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def XMotorsNo_changed(self):
        tot_XDrivers = int(self.XMotorsNo.currentText())        

        if tot_XDrivers == 1 : 
            self.X2_Driver.setEnabled(False)
            config.set('Configuration.h', 'x_motors','1')

        elif tot_XDrivers == 2 : 
            self.X2_Driver.setEnabled(True)  
            self.X2Current.setEnabled(True)
            self.X2Microsteps.setEnabled(True)
            self.X2Rence.setEnabled(True)   
            config.set('Configuration.h', 'x_motors','2')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  End selection of X Driver comboboxes  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

