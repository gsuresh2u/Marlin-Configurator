import sys 
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QPushButton, QMessageBox, QWidget, QLabel

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import webbrowser 

import os
import shutil
from os import path
import fileinput

import configparser
from configparser import SafeConfigParser
import io
import re

import Sanity_Check
from Sanity_Check import read_environments, read_boards, read_drivers


from Config import configfile, default_envs, motherboard, serial_port, baudrate, serial_port_2, serial_port_3,  x_motors, y_motors, z_motors, extruders
from Config import x_driver_type, x2_driver_type, y_driver_type, y2_driver_type, z_driver_type, z2_driver_type, z3_driver_type, z4_driver_type, \
    e0_driver_type, e1_driver_type, e2_driver_type, e3_driver_type, e4_driver_type, e5_driver_type, e6_driver_type, e7_driver_type

from Config import temp_sensor_0, temp_sensor_1, temp_sensor_2, temp_sensor_3, temp_sensor_4, temp_sensor_5, \
    temp_sensor_6, temp_sensor_bed, hotend_overshoot, bed_overshoot, cooler_overshoot

from Config import use_xmin_plug, use_ymin_plug, use_zmin_plug, use_xmax_plug, use_ymax_plug, use_zmax_plug, \
    xmin_endstop_invert, ymin_endstop_invert, zmin_endstop_invert, xmax_endstop_invert, ymax_endstop_invert, zmax_endstop_invert, zprobe_invert

from Config import xsteps_per_unit, ysteps_per_unit, zsteps_per_unit,e0steps_per_unit, x_max_feedrate, y_max_feedrate, z_max_feedrate, e0_max_feedrate, \
    x_max_acceleration, y_max_acceleration, z_max_acceleration, e0_max_acceleration, \
    invert_x_dir, invert_y_dir, invert_z_dir, invert_e0_dir, x_homing_position, y_homing_position, z_homing_position

from Config import x_bed_size, y_bed_size, x_min_position, y_min_position, z_height

from Config import z_min_uses_zendstop_pin, use_probe_for_z_homing, use_fixed_mounted_probe, use_nozzle_as_probe, use_bltouch, use_sensorless_probing, \
    probing_margin, use_multiple_probing, use_extra_probing, probe_x_offset, probe_y_offset, probe_z_offset, use_probing_heaters_off, \
    use_preheat_before_home, use_z_safe_homing

from Config import leveling_3point, leveling_linear, leveling_bilinear, leveling_ubl, leveling_mesh, \
    linear_points, ubl_points, mesh_points, restore_after_g28, preheat_before_level, g26_mesh_validation, lcd_bed_levelling 

from Config import use_single_nozzle, use_switching_extruder, use_switching_nozzle,use_parking_extruder, use_mixing_extruder, \
    mixing_extruder_no, nozzle_park_feature, nozzle_clean_feature  

from Config import use_psu_conrol, psu_state, wait_for_cooldown, auto_power_control, power_timeout, poweroff_temparature, display_type, printer_type

from Config import enable_eeprom, reset_on_errors, clear_old_values, use_print_counter, use_sd_support, individial_home_menu, \
    use_speaker, use_filament_sensor, filament_sensor_state 

from Config import extruder_runout_prevent, use_controller_fan, fast_pwm_fan, extruder_auto_fan_temp, use_bltouch_high_speed, use_z_steppers_auto_align, \
    use_adaptive_step_smoothing, use_powerloss_recovery  
    
from Config import use_linear_advance, linear_advance_kfactor, use_g29_retry_recover, long_filename_support, scroll_long_filename 

from Config import enable_baby_stepping, inegrated_baby_stepping, baby_step_without_homing, baby_step_always_available, baby_step_on_xy

from Config import enable_dual_x_carriage, dualx_x2_min_position, dualx_x2_max_position, dualx_duplication_offset, advanced_pause_feature, monitor_driver_status 

from Config import enable_x_input_shapping, x_input_shapping_frequency, x_input_shapping_zeta, enable_y_input_shapping, y_input_shapping_frequency, y_input_shapping_zeta

from Config import x_current, x_micro_steps, x_rense, x2_current, x2_micro_steps, x2_rense, y_current, y_micro_steps, y_rense, y2_current, y2_micro_steps, \
    y2_rense, z_current, z_micro_steps, z_rense, z2_current, z2_micro_steps, z2_rense, z3_current, z3_micro_steps, z3_rense, z4_current, z4_micro_steps, z4_rense  

from Config import tx_buffer_size, use_emergency_parcer, use_advanced_ok, sensorless_homing, use_tmc_debugging, chopper_voltage  
from Config import e0_current, e0_micro_steps, e0_rense, e1_current, e1_micro_steps, e1_rense, e2_current, e2_micro_steps, e2_rense         
from Config import e3_current, e3_micro_steps, e3_rense, e4_current, e4_micro_steps, e4_rense, e5_current, e5_micro_steps, e5_rense           
from Config import e6_current, e6_micro_steps, e6_rense, e7_current, e7_micro_steps, e7_rense 



    
SourceDir = "Original Configs/"
Modified  = str("   //Modified  ")

config = configparser.ConfigParser(allow_no_value=True)
config.read(configfile)
 
class MyWindow(QtWidgets.QDialog):
    def __init__(self):
        super(MyWindow,self).__init__()
        uic.loadUi('Marlin.ui',self)

        #QtWidgets.QComboBox.findText
        #self.Environment.clear()
        #Add all Environments to combobox
        self.Environments = read_environments()
        for Environments in self.Environments:
            self.Environment.addItem(Environments)
        self.Environment.setItemText(0, default_envs) # Set Default Environment from Config.ini file

        #Add all Motherboards to combobox
        self.Boards = read_boards()
        for Boards in self.Boards:
            self.BoardTxt.addItem(Boards)
        self.BoardTxt.setItemText(0, motherboard)  # Show motherboard from Config.ini file 

        #Add all Drivers to combobox
        self.Drivers = read_drivers()
        for Drivers in self.Drivers:
            self.X_Driver.addItem(Drivers)
            self.X2_Driver.addItem(Drivers)
            self.Y_Driver.addItem(Drivers)
            self.Y2_Driver.addItem(Drivers)
            self.Z_Driver.addItem(Drivers)
            self.Z2_Driver.addItem(Drivers)
            self.Z3_Driver.addItem(Drivers)
            self.Z4_Driver.addItem(Drivers)
            self.E0_Driver.addItem(Drivers)
            self.E1_Driver.addItem(Drivers)
            self.E2_Driver.addItem(Drivers)
            self.E3_Driver.addItem(Drivers)
            self.E4_Driver.addItem(Drivers)
            self.E5_Driver.addItem(Drivers)
            self.E6_Driver.addItem(Drivers)
            self.E7_Driver.addItem(Drivers)

        self.X_Driver.setItemText(0, x_driver_type)
        self.X2_Driver.setItemText(0, x2_driver_type) 
        self.Y_Driver.setItemText(0, y_driver_type)
        self.Y2_Driver.setItemText(0, y2_driver_type)
        self.Z_Driver.setItemText(0, z_driver_type)
        self.Z2_Driver.setItemText(0, z2_driver_type)
        self.Z3_Driver.setItemText(0, z3_driver_type)
        self.Z4_Driver.setItemText(0, z4_driver_type)
        self.E0_Driver.setItemText(0, e0_driver_type)
        self.E1_Driver.setItemText(0, e1_driver_type)
        self.E2_Driver.setItemText(0, e2_driver_type)
        self.E3_Driver.setItemText(0, e3_driver_type)
        self.E4_Driver.setItemText(0, e4_driver_type)
        self.E5_Driver.setItemText(0, e5_driver_type)
        self.E6_Driver.setItemText(0, e6_driver_type)
        self.E7_Driver.setItemText(0, e7_driver_type)
        
        self.Serial0.setCurrentText(serial_port)
        if serial_port_2 != "none" :
            self.Serial2.setCurrentText(serial_port_2)
        if serial_port_3 != "none" :
            self.Serial3.setCurrentText(serial_port_3)
        self.BaudRate.setCurrentText(baudrate) 
        self.XMotorsNo.setCurrentText(x_motors) 
        self.YMotorsNo.setCurrentText(y_motors)
        self.ZMotorsNo.setCurrentText(z_motors)
        self.Extruders.setCurrentText(extruders)


        #Sanity_Check.Conditions() # Need to Seperate below conditions to Sanity_Check.py file

        self.MixingSteppers.setEnabled(False)  # Disable Mixing Steppers by default

        self.PSUState.setEnabled(False)     # Disable PSU state by default
        self.WaitForCool.setEnabled(False)  # Disable PSU Wait for Cool by default
        self.AuPowControl.setEnabled(False) # Disable PSU Auto Power Control by default
        self.PowerTimeOut.setEnabled(False) # Disable PSU Timeout by default
        self.PowerOffTemp.setEnabled(False) # Disable PSU Poer off Temparature by default

        self.XMotorsNo.currentTextChanged.connect(self.XMotorsNo_changed)
        self.YMotorsNo.currentTextChanged.connect(self.YMotorsNo_changed)
        self.ZMotorsNo.currentTextChanged.connect(self.ZMotorsNo_changed)
        self.Extruders.currentTextChanged.connect(self.extruders_changed)

        #~~~~~~~~~~~~~~ Levelling Options ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.LinearPoints.setEnabled(False)         # Disable Linear Points by default
        self.UBLLevelPoints.setEnabled(True)        # Enable UBL Points by default
        self.MeshLevelPoints.setEnabled(False)      # Disable Mesh Points by default
        self.LinearPoints.setText("") 
        self.MeshLevelPoints.setText("") 

        self.Level3Point.toggled.connect(self.check_levelState)
        self.Linear.toggled.connect(self.check_levelState)
        self.BiLinear.toggled.connect(self.check_levelState)
        self.UBL.toggled.connect(self.check_levelState)
        self.MeshBed.toggled.connect(self.check_levelState)
        self.LevelHelpBtn.clicked.connect(self.OpenLevelHelpUrl)

        #~~~~~~~~~~~~~~ Probe Options ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.MultipleProbing.stateChanged.connect(self.check_Probing)  
        self.ZHelpBtn.clicked.connect(self.OpenZHelpUrl)

        
        # ~~~~~~~~~~~~~~ Endstops Options ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.UseXMinPlug.stateChanged.connect(self.check_xmin_endstop)
        self.UseYMinPlug.stateChanged.connect(self.check_ymin_endstop)
        self.UseZMinPlug.stateChanged.connect(self.check_zmin_endstop)
        self.UseXMinPlug.stateChanged.connect(self.check_xmin_endstop)
        self.UseXMaxPlug.stateChanged.connect(self.check_xmax_endstop)
        self.UseYMaxPlug.stateChanged.connect(self.check_ymax_endstop)
        self.UseZMaxPlug.stateChanged.connect(self.check_zmax_endstop)
        if self.UseXMinPlug.isChecked() == False :
            self.InvertXMinEndstop.setEnabled(False)
        if self.UseYMinPlug.isChecked() == False :
            self.InvertYMinEndstop.setEnabled(False)
        if self.UseZMinPlug.isChecked() == False :
            self.InvertZMinEndstop.setEnabled(False)
        if self.UseXMaxPlug.isChecked() == False :
            self.InvertXMaxEndstop.setEnabled(False)
        if self.UseYMaxPlug.isChecked() == False :
            self.InvertYMaxEndstop.setEnabled(False)
        if self.UseZMaxPlug.isChecked() == False :
            self.InvertZMaxEndstop.setEnabled(False)

        #~~~~~~~~~~~~~~ Nozzle Options ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.SingleNozzle.toggled.connect(self.check_Nozzle)
        self.SwichExruder.toggled.connect(self.check_Nozzle)
        self.SwichNozzle.toggled.connect(self.check_Nozzle)
        self.ParkExtruder.toggled.connect(self.check_Nozzle)
        self.MixExtruder.toggled.connect(self.check_Nozzle)
        self.MixingSteppers.setEnabled(False) 
        self.MixingSteppers.setText("") 
        self.NozzleHelpBtn.clicked.connect(self.OpenNozzleHelpUrl)



        #~~~~~~~~~~~~~~ PSU Control Options ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.PSUControl.stateChanged.connect(self.check_psuState)
        self.PowerTimeOut.setText("")
        self.PowerOffTemp.setText("")
        self.PSUHelpBtn.clicked.connect(self.OpenPSUHelpUrl)

        #~~~~~~~~~~~~~~ Additional Options ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.EnableEeprom.stateChanged.connect(self.check_eepromState) 
        self.FilamentSensor.stateChanged.connect(self.check_FilamenState) 
        self.FiSenState.setEnabled(False)

        self.AdvPause.stateChanged.connect(self.check_AdvPauseCheck) 

        self.ZAutoAlign.stateChanged.connect(self.check_auto_z_alien) 

        #QtWidgets.QComboBox.setCurrentText
       
        self.LA_KFactor.setEnabled(False)
        self.LAAvailable.stateChanged.connect(self.check_linearAdvance)
        self.TXBufferSize.setCurrentText(tx_buffer_size)

        
        if use_emergency_parcer == "on" :
            self.EmeParser.setChecked(True)
        if use_advanced_ok == "on" :
            self.AdvancedOK.setChecked(True)
        if advanced_pause_feature == "on" :
            self.AdvPause.setChecked(True)
        if monitor_driver_status == "on" :
            self.MoDriverStatus.setChecked(True)
        if sensorless_homing == "on" :
            self.SenLessHome.setChecked(True)
        if use_tmc_debugging == "on" :
            self.TMCDebug.setChecked(True)
        self.ChoVoltage.setCurrentText(chopper_voltage)
        

       #~~~~~~~~~~~  Baby Stepping Options ~~~~~~~~~~~~~
        self.IntiBabyStepping.setEnabled(False)
        self.BabyStepWOHome.setEnabled(False)
        self.BabyStepAlwAvail.setEnabled(False)
        self.BabyStepXY.setEnabled(False)
        self.BabyStepping.stateChanged.connect(self.check_babystepping)
        self.BaStepHelpBtn.clicked.connect(self.OpenBaStepHelpUrl)

        #~~~~~~~~~~~  Diable Dual-X  Options  by Defaultc~~~~~~~~~~~~~
        self.X2MinPosition.setEnabled(False)
        self.X2MaxPosition.setEnabled(False)
        self.DupliOffset.setEnabled(False)
        self.DualXEnable.stateChanged.connect(self.check_dualXstate) 
        self.DualXHelpBtn.clicked.connect(self.OpenDualXHelpUrl)

        #~~~~~~~~~~~  Diable Input Shappingby Default ~~~~~~~~~~~~~
        self.XInShapeFreq.setEnabled(False)
        self.XInShapeZeta.setEnabled(False)
        self.YInShapeFreq.setEnabled(False)
        self.YInShapeZeta.setEnabled(False)
        self.InputShappingX.stateChanged.connect(self.check_inputShapeX)
        self.InputShappingY.stateChanged.connect(self.check_inputShapeY)

        #~~~~~~~~~~~ Disable Current and Microsteps by Default ~~~~~~~~~~~~~
        self.X2Current.setEnabled(False)
        self.X2Microsteps.setEnabled(False)
        self.X2Rence.setEnabled(False)
        self.Y2Current.setEnabled(False)
        self.Y2Microsteps.setEnabled(False)
        self.Y2Rence.setEnabled(False)
        self.Z2Current.setEnabled(False)
        self.Z2Microsteps.setEnabled(False)
        self.Z2Rence.setEnabled(False)
        self.Z3Current.setEnabled(False)
        self.Z3Microsteps.setEnabled(False)
        self.Z3Rence.setEnabled(False)
        self.Z4Current.setEnabled(False)
        self.Z4Microsteps.setEnabled(False)
        self.Z4Rence.setEnabled(False)
        self.E1Current.setEnabled(False)
        self.E1Microsteps.setEnabled(False)
        self.E1Rence.setEnabled(False)
        self.E2Current.setEnabled(False)
        self.E2Microsteps.setEnabled(False)
        self.E2Rence.setEnabled(False)
        self.E3Current.setEnabled(False)
        self.E3Microsteps.setEnabled(False)
        self.E3Rence.setEnabled(False)
        self.E4Current.setEnabled(False)
        self.E4Microsteps.setEnabled(False)
        self.E4Rence.setEnabled(False)
        self.E5Current.setEnabled(False)
        self.E5Microsteps.setEnabled(False)
        self.E5Rence.setEnabled(False)
        self.E6Current.setEnabled(False)
        self.E6Microsteps.setEnabled(False)
        self.E6Rence.setEnabled(False)
        self.E7Current.setEnabled(False)
        self.E7Microsteps.setEnabled(False)
        self.E7Rence.setEnabled(False)
        self.CalculateBtn.clicked.connect(self.CalcCurrent)
        


        #Add all Displays to combobox
        #self.AllDisplays = read_displays()
        #for AllDisplays in self.AllDisplays:
        #    self.Display.addItem(AllDisplays)

        # Restoring Display and Priner type
        self.PrinterType.setCurrentText(printer_type)
        #self.Display.setCurrentText(display_type)

        
        # Show  Driver_types from Config.ini file
        #self.X_Driver.setCurrentText(x_driver_type)
        if int(self.XMotorsNo.currentText()) == 1 :
            self.X2_Driver.setEnabled(False)
        if int(self.XMotorsNo.currentText()) == 2 :
            self.X2_Driver.setCurrentText(x2_driver_type)

        self.Y_Driver.setCurrentText(y_driver_type)
        if int(self.YMotorsNo.currentText()) == 1 :
            self.Y2_Driver.setEnabled(False)
        if int(self.YMotorsNo.currentText()) == 2 :
            self.Y2_Driver.setEnabled(True)
            self.Y2_Driver.setCurrentText(y2_driver_type)

        self.Z_Driver.setCurrentText(z_driver_type)
        if int(self.ZMotorsNo.currentText()) == 1 :
            self.Z2_Driver.setEnabled(False)
            self.Z3_Driver.setEnabled(False)
            self.Z4_Driver.setEnabled(False)
        if int(self.ZMotorsNo.currentText()) == 2 :
            self.Z2_Driver.setEnabled(True)
            self.Z3_Driver.setEnabled(False)
            self.Z4_Driver.setEnabled(False)
            self.Z2_Driver.setCurrentText(z2_driver_type)
        if int(self.ZMotorsNo.currentText()) == 3 :
            self.Z2_Driver.setEnabled(True)
            self.Z3_Driver.setEnabled(True)
            self.Z4_Driver.setEnabled(False)
            self.Z2_Driver.setCurrentText(z2_driver_type)   
            self.Z3_Driver.setCurrentText(z3_driver_type)
        if int(self.ZMotorsNo.currentText()) == 4 :
            self.Z2_Driver.setEnabled(True)
            self.Z3_Driver.setEnabled(True)
            self.Z4_Driver.setEnabled(True)
            self.Z2_Driver.setCurrentText(z2_driver_type)   
            self.Z3_Driver.setCurrentText(z3_driver_type)   
            self.Z4_Driver.setCurrentText(z4_driver_type) 

        if int(self.Extruders.currentText()) == 1 :
            self.E1_Driver.setEnabled(False)
            self.E2_Driver.setEnabled(False)
            self.E3_Driver.setEnabled(False)
            self.E4_Driver.setEnabled(False)
            self.E5_Driver.setEnabled(False)
            self.E6_Driver.setEnabled(False)
            self.E7_Driver.setEnabled(False)
            self.E0_Driver.setCurrentText(e0_driver_type)

        if int(self.Extruders.currentText()) == 2 :
            self.E2_Driver.setEnabled(False)
            self.E3_Driver.setEnabled(False)
            self.E4_Driver.setEnabled(False)
            self.E5_Driver.setEnabled(False)
            self.E6_Driver.setEnabled(False)
            self.E7_Driver.setEnabled(False)
            self.E0_Driver.setCurrentText(e0_driver_type)   
            self.E1_Driver.setCurrentText(e1_driver_type) 
        if int(self.Extruders.currentText()) == 3 :
            self.E3_Driver.setEnabled(False)
            self.E4_Driver.setEnabled(False)
            self.E5_Driver.setEnabled(False)
            self.E6_Driver.setEnabled(False)
            self.E7_Driver.setEnabled(False)
            self.E0_Driver.setCurrentText(e0_driver_type)   
            self.E1_Driver.setCurrentText(e1_driver_type)
            self.E2_Driver.setCurrentText(e2_driver_type) 
        if int(self.Extruders.currentText()) == 4 :
            self.E4_Driver.setEnabled(False)
            self.E5_Driver.setEnabled(False)
            self.E6_Driver.setEnabled(False)
            self.E7_Driver.setEnabled(False)
            self.E0_Driver.setCurrentText(e0_driver_type)   
            self.E1_Driver.setCurrentText(e1_driver_type)
            self.E2_Driver.setCurrentText(e2_driver_type)    
            self.E3_Driver.setCurrentText(e3_driver_type)
            print("e4") 
        if int(self.Extruders.currentText()) == 5 :
            self.E5_Driver.setEnabled(False)
            self.E6_Driver.setEnabled(False)
            self.E7_Driver.setEnabled(False)
            self.E0_Driver.setCurrentText(e0_driver_type)   
            self.E1_Driver.setCurrentText(e1_driver_type)
            self.E2_Driver.setCurrentText(e2_driver_type)    
            self.E3_Driver.setCurrentText(e3_driver_type) 
            self.E4_Driver.setCurrentText(e4_driver_type)
        if int(self.Extruders.currentText()) == 6 :
            self.E6_Driver.setEnabled(False)
            self.E7_Driver.setEnabled(False)
            self.E0_Driver.setCurrentText(e0_driver_type)   
            self.E1_Driver.setCurrentText(e1_driver_type)
            self.E2_Driver.setCurrentText(e2_driver_type)    
            self.E3_Driver.setCurrentText(e3_driver_type) 
            self.E4_Driver.setCurrentText(e4_driver_type)  
            self.E5_Driver.setCurrentText(e5_driver_type) 
        if int(self.Extruders.currentText()) == 7 :
            self.E7_Driver.setEnabled(False)
            self.E0_Driver.setCurrentText(e0_driver_type)   
            self.E1_Driver.setCurrentText(e1_driver_type)
            self.E2_Driver.setCurrentText(e2_driver_type)    
            self.E3_Driver.setCurrentText(e3_driver_type) 
            self.E4_Driver.setCurrentText(e4_driver_type)  
            self.E5_Driver.setCurrentText(e5_driver_type)
            self.E6_Driver.setCurrentText(e6_driver_type) 
        if int(self.Extruders.currentText()) == 8 :
            self.E0_Driver.setCurrentText(e0_driver_type)   
            self.E1_Driver.setCurrentText(e1_driver_type)
            self.E2_Driver.setCurrentText(e2_driver_type)    
            self.E3_Driver.setCurrentText(e3_driver_type) 
            self.E4_Driver.setCurrentText(e4_driver_type)  
            self.E5_Driver.setCurrentText(e5_driver_type)
            self.E6_Driver.setCurrentText(e6_driver_type)
            self.E7_Driver.setCurrentText(e7_driver_type) 

        # Restore Temparature Sensors from ini file
        self.TempSensor0.setCurrentText(temp_sensor_0)
        self.TempSensor1.setCurrentText(temp_sensor_1)
        self.TempSensor2.setCurrentText(temp_sensor_2)
        self.TempSensor3.setCurrentText(temp_sensor_3)
        self.TempSensor4.setCurrentText(temp_sensor_4)
        self.TempSensor5.setCurrentText(temp_sensor_5)
        self.TempSensor6.setCurrentText(temp_sensor_6)
        self.TempSensorBed.setCurrentText(temp_sensor_bed)

        self.HotendOvershoot.setText(hotend_overshoot)
        self.BedOvershoot.setText(bed_overshoot)
        self.CoolerOvershoot.setText(cooler_overshoot)
            

        # Endstops Usage Status ~~~~~~~~~~~~~~~~~~
        if use_xmin_plug == "on" :
            self.UseXMinPlug.setChecked(True)
        if use_ymin_plug == "on" :
            self.UseYMinPlug.setChecked(True)
        if use_zmin_plug == "on" :
            self.UseZMinPlug.setChecked(True)
        if use_xmax_plug == "on" :
            self.UseXMaxPlug.setChecked(True)
        if use_ymax_plug == "on" :
            self.UseYMaxPlug.setChecked(True)
        if use_zmax_plug == "on" :
            self.UseZMaxPlug.setChecked(True)

        # Endstops Invering Status ~~~~~~~~~~~~~~~~
        if xmin_endstop_invert == "true" :
            self.InvertXMinEndstop.setChecked(False)
        if ymin_endstop_invert == "true" :
            self.InvertYMinEndstop.setChecked(True)
        if zmin_endstop_invert == "true" :
            self.InvertZMinEndstop.setChecked(True)
        if xmax_endstop_invert == "true" :
            self.InvertXMaxEndstop.setChecked(True)
        if ymax_endstop_invert == "true" :
            self.InvertYMaxEndstop.setChecked(True)
        if zmax_endstop_invert == "true" :
            self.InvertZMaxEndstop.setChecked(True)
        if zprobe_invert == "true" :
            self.InvertProbeEndstop.setChecked(True)

        # Restoring Steps per Unit from ini file ~~~~~~~~~~~~~~~~
        self.XSteps.setText(xsteps_per_unit)
        self.YSteps.setText(ysteps_per_unit)
        self.ZSteps.setText(zsteps_per_unit)
        self.E0Steps.setText(e0steps_per_unit)

        # Restoring Max Feedrate from ini file ~~~~~~~~~~~~~~~~
        self.XMaxFeedRate.setText(x_max_feedrate)
        self.YMaxFeedRate.setText(y_max_feedrate)
        self.ZMaxFeedRate.setText(z_max_feedrate)
        self.E0MaxFeedRate.setText(e0_max_feedrate)

        # Restoring Max Accleraion from ini file ~~~~~~~~~~~~~~~~
        self.XMaxAccleration.setText(x_max_acceleration)
        self.YMaxAccleration.setText(y_max_acceleration)
        self.ZMaxAccleration.setText(z_max_acceleration)
        self.E0MaxAccleration.setText(e0_max_acceleration)

        # Restoring Axis Inverting from ini file ~~~~~~~~~~~~~~~~
        self.InvertXAxis.setCurrentText(invert_x_dir)
        self.InvertYAxis.setCurrentText(invert_y_dir)
        self.InvertZAxis.setCurrentText(invert_z_dir)
        self.InvertE0Axis.setCurrentText(invert_e0_dir)

        # Restoring Axis Homing position from ini file ~~~~~~~~~~~~~~~~
        self.XHoming.setCurrentText(x_homing_position)
        self.YHoming.setCurrentText(y_homing_position)
        self.ZHoming.setCurrentText(z_homing_position)

        # Restoring Bed size from ini file ~~~~~~~~~~~~~~~~
        self.XBedSize.setText(x_bed_size)
        self.YBedSize.setText(y_bed_size)
        self.ZHeight.setText(z_height)
        self.XMinPosittion.setText(x_min_position)
        self.YMinPosittion.setText(y_min_position)

        

        # Restoring Z-Probe options from ini file ~~~~~~~~~~~~~~~~
        if z_min_uses_zendstop_pin == "on" :
            self.ZProbeUsesZMin.setChecked(True)
        if use_probe_for_z_homing == "on" :
            self.UseProbeZHome.setChecked(True)
        if use_fixed_mounted_probe == "on" :
            self.FixedProbe.setChecked(True)
        if use_nozzle_as_probe == "on" :
            self.NozzleasProbe.setChecked(True)
        if use_bltouch == "on" :
            self.BLTtouch.setChecked(True)
        if use_sensorless_probing == "on" :
            self.SenLessProbing.setChecked(True)
            #probing_margin             = 10
        if use_multiple_probing == "on" :
            self.MultipleProbing.setChecked(True)
        if use_extra_probing == "on" :
            self.ExtraProbing.setChecked(True)

        self.ProbeXOffset.setText(probe_x_offset)                
        self.ProbeYOffset.setText(probe_y_offset)             
        self.ProbeZOffset.setText(probe_z_offset) 
         
        if use_probing_heaters_off  == "on" :
            self.ProbeHeatOff.setChecked(True)
        if use_preheat_before_home == "on" :
            self.PreHeatHoming.setChecked(True)

        if use_z_safe_homing == "on" :
            self.ZSafeHome.setChecked(True)
        
        # Restoring Levelling options from ini file ~~~~~~~~~~~~~~~~
        if leveling_3point == "on" :
            self.Level3Point.setChecked(True)
        if leveling_linear == "on" :
            self.Linear.setChecked(True)
        if leveling_bilinear == "on" :
            self.BiLinear.setChecked(True)
        if leveling_ubl == "on" :
            self.UBL.setChecked(True)
        if leveling_mesh == "on" :
            self.MeshBed.setChecked(True)
        self.LinearPoints.setText(linear_points)
        self.UBLLevelPoints.setText(ubl_points)
        self.MeshLevelPoints.setText(mesh_points)
        if restore_after_g28 == "on" :
            self.RestoreAfterG28.setChecked(True) 
        if preheat_before_level == "on" :
            self.PreHeatLevel.setChecked(True)
        if g26_mesh_validation == "on" :
            self.G26MeshValid.setChecked(True)
        if lcd_bed_levelling == "on" :
            self.LcdBedLevel.setChecked(True)

        # Restoring Nozzle options from ini file ~~~~~~~~~~~~~~~~~~
        if use_single_nozzle == "on" :
            self.SingleNozzle.setChecked(True)
        if use_switching_extruder == "on" :
            self.SwichExruder.setChecked(True)
        if use_switching_nozzle == "on" :
            self.SwichNozzle.setChecked(True)
        if use_parking_extruder == "on" :
            self.ParkExtruder.setChecked(True)
        if use_mixing_extruder == "on" :
            self.MixExtruder.setChecked(True)
        self.MixingSteppers.setText(mixing_extruder_no)
        if nozzle_park_feature == "on" :
            self.NozParkFeature.setChecked(True)
        if nozzle_clean_feature == "on" :
            self.NozCleanFeature.setChecked(True)

        # Restoring PSU-Conrol options from ini file ~~~~~~~~~~~~~~~~~~
        if use_psu_conrol == "on" :
            self.PSUControl.setChecked(True)
        if psu_state == "low" :
            self.PSUState.setCurrentText("LOW")
        if psu_state == "high" :
            self.PSUState.setCurrentText("HIGH")
        if wait_for_cooldown == "on" :
            self.WaitForCool.setChecked(True)
        if auto_power_control == "on" :
            self.AuPowControl.setChecked(True)
        self.PowerTimeOut.setText(power_timeout)
        self.PowerOffTemp.setText(poweroff_temparature)

        # Restoring Additional options from ini file ~~~~~~~~~~~~~~~~~~
        if enable_eeprom == "on" :
            self.EnableEeprom.setChecked(True)
        if reset_on_errors == "on" :
            self.EepromReset.setChecked(True)
        if clear_old_values == "on" :
            self.EepromClear.setChecked(True)
        if use_print_counter == "on" :
            self.PrintCounter.setChecked(True)
        if use_sd_support == "on" :
            self.SDSupport.setChecked(True)
        if individial_home_menu == "on" :
            self.InAxisHoMenu.setChecked(True)
        if use_speaker == "on" :
            self.Speaker.setChecked(True)
        if use_filament_sensor == "on" :
            self.FilamentSensor.setChecked(True)
        if filament_sensor_state == "low" :
            self.FiSenState.setCurrentText("LOW")
        if filament_sensor_state == "high" :
            self.FiSenState.setCurrentText("HIGH")

         
        # Seting Values Configuration_adv.h from ini 
        if extruder_runout_prevent == "on" :
            self.ExRunoutPrevent.setChecked(True)
        if use_controller_fan == "on" :
            self.UseConrollerFan.setChecked(True)
        if fast_pwm_fan == "on" :
            self.FastPWMFan.setChecked(True)
        self.ExAutoFanTemp.setText(extruder_auto_fan_temp)
        if use_bltouch_high_speed == "on" :
            self.BLTouchHighSpeed.setChecked(True)
        if use_z_steppers_auto_align == "on" :
            self.ZAutoAlign.setChecked(True)
        if use_adaptive_step_smoothing == "on" :
            self.AdStepSmooth.setChecked(True)
        if use_powerloss_recovery == "on" :  
            self.PowLossRecover.setChecked(True)
    
        if use_linear_advance == "on" :
            self.LAAvailable.setChecked(True)
        self.LA_KFactor.setText(linear_advance_kfactor)
        if use_g29_retry_recover == "on" :
            self.G29RetryRecover.setChecked(True)
        if long_filename_support == "on" :
            self.LongFileName.setChecked(True)
        if scroll_long_filename == "on" :
            self.ScrolLongFile.setChecked(True)

        # Baby Stepping 
        if enable_baby_stepping == "on" :
            self.BabyStepping.setChecked(True)
        if inegrated_baby_stepping == "on" :
            self.IntiBabyStepping.setChecked(True)
        if baby_step_without_homing == "on" :
            self.BabyStepWOHome.setChecked(True)
        if baby_step_always_available == "on" :
            self.BabyStepAlwAvail.setChecked(True)
        if baby_step_on_xy == "on" :
            self.BabyStepXY.setChecked(True)

        # Dual-X Carriage 
        if enable_dual_x_carriage == "on" :
            self.DualXEnable.setChecked(True)
            self.X2MinPosition.setText(dualx_x2_min_position)
            self.X2MaxPosition.setText(dualx_x2_max_position)
            self.DupliOffset.setText(dualx_duplication_offset)
        else : 
            self.DualXEnable.setChecked(False)

        # Input Shapping
        if enable_x_input_shapping == "on" :
            self.InputShappingX.setChecked(True)
        self.XInShapeFreq.setText(x_input_shapping_frequency)
        self.XInShapeZeta.setText(x_input_shapping_zeta)
        if enable_y_input_shapping == "on" :
            self.InputShappingY.setChecked(True)
        self.YInShapeFreq.setText(y_input_shapping_frequency)
        self.YInShapeZeta.setText(y_input_shapping_zeta)

        # Steppers Curren & Microsteps
        self.XCurrent.setText(x_current)
        self.XMicrosteps.setCurrentText(x_micro_steps)
        self.XRence.setText(x_rense)
        self.X2Current.setText(x2_current)
        self.X2Microsteps.setCurrentText(x2_micro_steps)
        self.X2Rence.setText(x2_rense)
        self.YCurrent.setText(y_current)            
        self.YMicrosteps.setCurrentText(y_micro_steps)       
        self.YRence.setText(y_rense)             
        self.Y2Current.setText(y2_current)        
        self.Y2Microsteps.setCurrentText(y2_micro_steps)      
        self.Y2Rence.setText(y2_rense)          
        self.ZCurrent.setText(z_current)           
        self.ZMicrosteps.setCurrentText(z_micro_steps)     
        self.ZRence.setText(z_rense)            
        self.Z2Current.setText(z2_current)        
        self.Z2Microsteps.setCurrentText(z2_micro_steps)      
        self.Z2Rence.setText(z2_rense)            
        self.Z3Current.setText(z3_current)          
        self.Z3Microsteps.setCurrentText(z3_micro_steps)     
        self.Z3Rence.setText(z3_rense)            
        self.Z4Current.setText(z4_current)         
        self.Z4Microsteps.setCurrentText(z4_micro_steps)     
        self.Z4Rence.setText(z4_rense)  

        self.E0Current.setText(e0_current)          
        self.E0Microsteps.setCurrentText(e0_micro_steps)      
        self.E0Rence.setText(e0_rense)            
        self.E1Current.setText(e1_current)          
        self.E1Microsteps.setCurrentText(e1_micro_steps)      
        self.E1Rence.setText(e1_rense)              
        self.E2Current.setText(e2_current)          
        self.E2Microsteps.setCurrentText(e2_micro_steps)      
        self.E2Rence.setText(e2_rense)            
        self.E3Current.setText(e3_current)          
        self.E3Microsteps.setCurrentText(e3_micro_steps)      
        self.E3Rence.setText(e3_rense)            
        self.E4Current.setText(e4_current)          
        self.E4Microsteps.setCurrentText(e4_micro_steps)      
        self.E4Rence.setText(e4_rense)            
        self.E5Current.setText(e5_current)          
        self.E5Microsteps.setCurrentText(e5_micro_steps)      
        self.E5Rence.setText(e5_rense)            
        self.E6Current.setText(e6_current)          
        self.E6Microsteps.setCurrentText(e6_micro_steps)      
        self.E6Rence.setText(e6_rense)            
        self.E7Current.setText(e7_current)          
        self.E7Microsteps.setCurrentText(e7_micro_steps)      
        self.E7Rence.setText(e7_rense) 
        


        #parser = configparser.ConfigParser()
        #parser.set('Configuration.h', 'extruders','5')

        #with open('Config.ini', 'wb') as Newconfigfile:
        #    parser.write(Newconfigfile)

        

        self.GenerateBtn.clicked.connect(self.GenarateFn)

        

        
        

    


    def OpenZHelpUrl(self) :
        webbrowser.open('https://marlinfw.org/docs/configuration/configuration.html#z-probe-options')

    def OpenLevelHelpUrl(self) :
        webbrowser.open('https://marlinfw.org/docs/configuration/configuration.html#bed-leveling')
    
    def OpenNozzleHelpUrl(self) :
        webbrowser.open('https://marlinfw.org/docs/configuration/configuration.html#single-nozzle')

    def OpenPSUHelpUrl(self) :
        webbrowser.open('https://marlinfw.org/docs/configuration/configuration.html#power-supply')

    def OpenDualXHelpUrl(self) :
        webbrowser.open('https://marlinfw.org/docs/configuration/configuration.html#dual-x-carriage')

    def OpenBaStepHelpUrl(self) :
        webbrowser.open('https://marlinfw.org/docs/configuration/configuration.html#babystepping')

    def GenarateFn(self):
        TargetDir = self.PrinterName.text() #Read current text in Printer Name
        try:
            os.mkdir(TargetDir) #Create Folder with name same as Printer Name
        except OSError:
            print ("Direcory Already Exists")
        else:
            print ("Successfully Created the directory %s " % TargetDir)
        
        #~~~~~~~~~~~~~~~~~~~~~~ Start Changing Environmen in platformio.ino File ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Newdata = (''.join(self.Environment.currentText())) #Get Current text in Envoronment Combobox'
        NewEnvironment = (''.join(Newdata.splitlines()))    #To Delete next line '\n'
        config.set('platformio', 'default_envs', NewEnvironment)
        NewEnvironment = "default_envs = "+ NewEnvironment
        f1 = open(SourceDir+'platformio.ini', 'r')
        f2 = open(TargetDir+'\platformio.ini', 'w')
        for line in f1:
            f2.write(line.replace("default_envs = mega2560", NewEnvironment))
        f1.close()
        f2.close()
        #~~~~~~~~~~~~~~~~~~~~~~ End Changing Environmen in platformio.ino File ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


        #~~~~~~~~~~~~~~~~~~~~~~ Start Changing in Configuration.h File ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        f1Read = open(SourceDir+'Configuration.h', 'r')
        f2Write = open(TargetDir+'\Configuration.h', 'w')
        ConfigFile  = TargetDir+'\Configuration.h'
        for line in f1Read:
            f2Write.write(line.replace("none, default config", self.AuthorTxt.text()))    # Changing Author Name
        f1Read.close()
        f2Write.close()

        with fileinput.FileInput(ConfigFile, inplace=True) as file:  
            NewBoard= (''.join(self.BoardTxt.currentText())) #Get Current text in BoardTxt Combobox'
            NewBoard = (''.join(NewBoard.splitlines()))    #To Delete next line '\n' 
            config.set('Configuration.h', 'motherboard', NewBoard)
            NewBoard = "#define MOTHERBOARD  " + "BOARD_"+NewBoard
            for line in file:
                print(line.replace("#define MOTHERBOARD ", NewBoard + Modified), end='')  # Changing MotherBoard
        

        NewSerial0 = (''.join(self.Serial0.currentText())) #Get Current text in Serial 0 Combobox'
        NewSerial0 = (''.join(NewSerial0.splitlines()))    #To Delete next line '\n'
        config.set('Configuration.h', 'serial_port', NewSerial0)
        with fileinput.FileInput(ConfigFile, inplace=True) as file:   
            for line in file:
                print(line.replace("#define SERIAL_PORT ", "#define SERIAL_PORT  "+ NewSerial0 + Modified), end='')  # Changing Serial 0
        

        NewSerial2 = (''.join(self.Serial2.currentText())) #Get Current text in Serial2 Combobox'
        NewSerial2 = (''.join(NewSerial2.splitlines()))    #To Delete next line '\n'
        config.set('Configuration.h', 'serial_port_2', NewSerial2)
        if NewSerial2 != "None" :
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define SERIAL_PORT_2 ", "#define SERIAL_PORT_2 "+ NewSerial2 + Modified), end='')  # Changing Serial 2


        NewSerial3 = (''.join(self.Serial3.currentText())) #Get Current text in Serial3 Combobox'
        NewSerial3 = (''.join(NewSerial3.splitlines()))    #To Delete next line '\n'
        config.set('Configuration.h', 'serial_port_3', NewSerial3)
        if NewSerial3 != "None" :
            print(NewSerial3)
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define SERIAL_PORT_3 ", "#define SERIAL_PORT_3 "+ NewSerial3 + Modified), end='')  # Changing Serial 3
        
        NewBaudRate = (''.join(self.BaudRate.currentText())) #Get Current text in BaudRate Combobox'
        NewBaudRate = (''.join(NewBaudRate.splitlines()))    #To Delete next line '\n'
        config.set('Configuration.h', 'baudrate', NewBaudRate)
        with fileinput.FileInput(ConfigFile, inplace=True) as file:   
            for line in file:
                print(line.replace("#define BAUDRATE ", "#define BAUDRATE "+ NewBaudRate + Modified), end='')  # Changing BaudRate

        NewXDriver= (''.join(self.X_Driver.currentText())) #Get Current text in X_Driver Combobox'
        NewXDriver = (''.join(NewXDriver.splitlines()))    #To Delete next line '\n' 
        config.set('Configuration.h', 'x_driver_type', NewXDriver) 
        with fileinput.FileInput(ConfigFile, inplace=True) as file:   
            for line in file:
                print(line.replace("#define X_DRIVER_TYPE", "#define X_DRIVER_TYPE  "+ NewXDriver + Modified), end='')  # Changing X Driver

        if self.X2_Driver.isEnabled()== True :
            NewX2Driver= (''.join(self.X2_Driver.currentText())) #Get Current text in X2_Driver Combobox'
            NewX2Driver = (''.join(NewX2Driver.splitlines()))    #To Delete next line '\n' 
            config.set('Configuration.h', 'x2_driver_type', NewX2Driver) 
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define X2_DRIVER_TYPE", "#define X2_DRIVER_TYPE  "+ NewX2Driver + Modified), end='')  # Changing X2 Driver
        else : config.set('Configuration.h', 'x2_driver_type', "") 

        NewYDriver= (''.join(self.Y_Driver.currentText())) #Get Current text in Y_Driver Combobox'
        NewYDriver = (''.join(NewYDriver.splitlines()))    #To Delete next line '\n'  
        config.set('Configuration.h', 'y_driver_type', NewYDriver) 
        with fileinput.FileInput(ConfigFile, inplace=True) as file:   
            for line in file:
                print(line.replace("#define Y_DRIVER_TYPE", "#define Y_DRIVER_TYPE  "+ NewYDriver + Modified), end='')  # Changing Y Driver

        if self.Y2_Driver.isEnabled() == True :
            NewY2Driver= (''.join(self.Y2_Driver.currentText())) #Get Current text in Y2_Driver Combobox'
            NewY2Driver = (''.join(NewY2Driver.splitlines()))    #To Delete next line '\n' 
            config.set('Configuration.h', 'y2_driver_type', NewY2Driver) 
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define Y2_DRIVER_TYPE", "#define Y2_DRIVER_TYPE  "+ NewY2Driver + Modified), end='')  # Changing Y2 Driver
        else : config.set('Configuration.h', 'y2_driver_type', "") 

        NewZDriver= (''.join(self.Z_Driver.currentText())) #Get Current text in Z_Driver Combobox'
        NewZDriver = (''.join(NewZDriver.splitlines()))    #To Delete next line '\n'  
        config.set('Configuration.h', 'z_driver_type', NewZDriver) 
        with fileinput.FileInput(ConfigFile, inplace=True) as file:   
            for line in file:
                print(line.replace("#define Z_DRIVER_TYPE", "#define Z_DRIVER_TYPE  "+ NewZDriver + Modified), end='')  # Changing Z Driver

        if self.Z2_Driver.isEnabled() == True :
            NewZ2Driver= (''.join(self.Z2_Driver.currentText())) #Get Current text in Z2_Driver Combobox'
            NewZ2Driver = (''.join(NewZ2Driver.splitlines()))    #To Delete next line '\n' 
            config.set('Configuration.h', 'z2_driver_type', NewZ2Driver) 
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define Z2_DRIVER_TYPE", "#define Z2_DRIVER_TYPE  "+ NewZ2Driver + Modified), end='')  # Changing Z2 Driver
        else : config.set('Configuration.h', 'z2_driver_type', "") 

        if self.Z3_Driver.isEnabled() == True :
            NewZ3Driver= (''.join(self.Z3_Driver.currentText())) #Get Current text in Z3_Driver Combobox'
            NewZ3Driver = (''.join(NewZ3Driver.splitlines()))    #To Delete next line '\n' 
            config.set('Configuration.h', 'z3_driver_type', NewZ3Driver) 
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define Z3_DRIVER_TYPE", "#define Z3_DRIVER_TYPE  "+ NewZ3Driver + Modified), end='')  # Changing Z3 Driver
        else : config.set('Configuration.h', 'z3_driver_type', "") 

        if self.Z4_Driver.isEnabled() == True :
            NewZ4Driver= (''.join(self.Z4_Driver.currentText())) #Get Current text in Z4_Driver Combobox'
            NewZ4Driver = (''.join(NewZ4Driver.splitlines()))    #To Delete next line '\n'
            config.set('Configuration.h', 'z4_driver_type', NewZ4Driver)  
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define Z4_DRIVER_TYPE", "#define Z4_DRIVER_TYPE  "+ NewZ4Driver + Modified), end='')  # Changing Z4 Driver
        else : config.set('Configuration.h', 'z4_driver_type', "")

        NewE0Driver= (''.join(self.E0_Driver.currentText())) #Get Current text in E0_Driver Combobox'
        NewE0Driver = (''.join(NewE0Driver.splitlines()))    #To Delete next line '\n' 
        config.set('Configuration.h', 'e0_driver_type', NewE0Driver) 
        with fileinput.FileInput(ConfigFile, inplace=True) as file:   
            for line in file:
                print(line.replace("#define E0_DRIVER_TYPE", "#define E0_DRIVER_TYPE    "+ NewE0Driver + Modified), end='')  # Changing E0 Driver

        if self.E1_Driver.isEnabled() == True :
            NewE1Driver= (''.join(self.E1_Driver.currentText())) #Get Current text in E1_Driver Combobox'
            NewE1Driver = (''.join(NewE1Driver.splitlines()))    #To Delete next line '\n'
            config.set('Configuration.h', 'e1_driver_type', NewE1Driver) 
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define E1_DRIVER_TYPE", "#define E1_DRIVER_TYPE    "+ NewE1Driver + Modified), end='')  # Changing E1 Driver
        else : config.set('Configuration.h', 'e1_driver_type', "")

        if self.E2_Driver.isEnabled() == True :
            NewE2Driver= (''.join(self.E2_Driver.currentText())) #Get Current text in E2_Driver Combobox'
            NewE2Driver = (''.join(NewE2Driver.splitlines()))    #To Delete next line '\n'
            config.set('Configuration.h', 'e2_driver_type', NewE2Driver)  
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define E2_DRIVER_TYPE", "#define E2_DRIVER_TYPE    "+ NewE2Driver + Modified), end='')  # Changing E2 Driver
        else : config.set('Configuration.h', 'e2_driver_type', "")

        if self.E3_Driver.isEnabled() == True :
            NewE3Driver= (''.join(self.E3_Driver.currentText())) #Get Current text in E3_Driver Combobox'
            NewE3Driver = (''.join(NewE3Driver.splitlines()))    #To Delete next line '\n' 
            config.set('Configuration.h', 'e3_driver_type', NewE3Driver) 
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define E3_DRIVER_TYPE", "#define E3_DRIVER_TYPE    "+ NewE3Driver + Modified), end='')  # Changing E3 Driver
        else : config.set('Configuration.h', 'e3_driver_type', "")

        if self.E4_Driver.isEnabled() == True :
            NewE4Driver= (''.join(self.E4_Driver.currentText())) #Get Current text in E4_Driver Combobox'
            NewE4Driver = (''.join(NewE4Driver.splitlines()))    #To Delete next line '\n' 
            config.set('Configuration.h', 'e4_driver_type', NewE4Driver) 
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define E4_DRIVER_TYPE", "#define E4_DRIVER_TYPE    "+ NewE4Driver + Modified), end='')  # Changing E4 Driver
        else : config.set('Configuration.h', 'e4_driver_type', "")

        if self.E5_Driver.isEnabled() == True :
            NewE5Driver= (''.join(self.E5_Driver.currentText())) #Get Current text in E5_Driver Combobox'
            NewE5Driver = (''.join(NewE5Driver.splitlines()))    #To Delete next line '\n' 
            config.set('Configuration.h', 'e5_driver_type', NewE5Driver) 
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define E5_DRIVER_TYPE", "#define E5_DRIVER_TYPE    "+ NewE5Driver + Modified), end='')  # Changing E5 Driver
        else : config.set('Configuration.h', 'e5_driver_type', "")

        if self.E6_Driver.isEnabled() == True :
            NewE6Driver= (''.join(self.E6_Driver.currentText())) #Get Current text in E6_Driver Combobox'
            NewE6Driver = (''.join(NewE6Driver.splitlines()))    #To Delete next line '\n' 
            config.set('Configuration.h', 'e6_driver_type', NewE6Driver) 
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define E6_DRIVER_TYPE", "#define E6_DRIVER_TYPE    "+ NewE6Driver + Modified), end='')  # Changing E6 Driver
        else : config.set('Configuration.h', 'e6_driver_type', "")

        if self.E7_Driver.isEnabled() == True :
            NewE7Driver= (''.join(self.E7_Driver.currentText())) #Get Current text in E7_Driver Combobox'
            NewE7Driver = (''.join(NewE7Driver.splitlines()))    #To Delete next line '\n'
            config.set('Configuration.h', 'e7_driver_type', NewE7Driver)  
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define E7_DRIVER_TYPE", "#define E7_DRIVER_TYPE    "+ NewE7Driver + Modified), end='')  # Changing E7 Driver
        else : config.set('Configuration.h', 'e7_driver_type', "")
    
        NewExtruders= (''.join(self.Extruders.currentText())) #Get Current text in Extruders Combobox'
        NewExtruders = (''.join(NewExtruders.splitlines()))    #To Delete next line '\n' 
        config.set('Configuration.h', 'extruders', NewExtruders) 
        with fileinput.FileInput(ConfigFile, inplace=True) as file:   
            for line in file:
                print(line.replace("#define EXTRUDERS", "#define EXTRUDERS "+ NewExtruders + Modified), end='')  # Changing Extruders Number

        if self.SingleNozzle.isChecked() == True :
            config.set('Configuration.h', 'use_single_nozzle', "on")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define SINGLENOZZLE", "#define SINGLENOZZLE"+ Modified), end='')  # Enabling Single Nozzle
        else :
            config.set('Configuration.h', 'use_single_nozzle', "off")

        # Temprature Sensors
        config.set('Configuration.h', 'temp_sensor_0', self.TempSensor0.currentText())
        config.set('Configuration.h', 'temp_sensor_1', self.TempSensor1.currentText())
        config.set('Configuration.h', 'temp_sensor_2', self.TempSensor2.currentText())
        config.set('Configuration.h', 'temp_sensor_3', self.TempSensor3.currentText())
        config.set('Configuration.h', 'temp_sensor_4', self.TempSensor4.currentText())
        config.set('Configuration.h', 'temp_sensor_5', self.TempSensor5.currentText())
        config.set('Configuration.h', 'temp_sensor_6', self.TempSensor6.currentText())
        config.set('Configuration.h', 'temp_sensor_bed', self.TempSensorBed.currentText())

        # Overshoot emparatures
        config.set('Configuration.h', 'hotend_overshoot', self.HotendOvershoot.text())
        config.set('Configuration.h', 'bed_overshoot', self.BedOvershoot.text())
        config.set('Configuration.h', 'cooler_overshoot', self.CoolerOvershoot.text())

        # Endstops ~~~~~~~~~~~
        if self.UseXMinPlug.isChecked() == False :
            config.set('Configuration.h', 'use_xmin_plug', "off")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("#define USE_XMIN_PLUG", "//#define USE_XMIN_PLUG"+ Modified), end='')  # Disabling X_Min Endstop
        else : 
            config.set('Configuration.h', 'use_xmin_plug', "on")

        if self.UseYMinPlug.isChecked() == False :
            config.set('Configuration.h', 'use_ymin_plug', "off")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("#define USE_YMIN_PLUG", "//#define USE_YMIN_PLUG"+ Modified), end='')  # Disabling Y_Min Endstop
        else : 
            config.set('Configuration.h', 'use_ymin_plug', "on")

        if self.UseXMaxPlug.isChecked() == True :
            config.set('Configuration.h', 'use_xmax_plug', "on")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define USE_XMAX_PLUG", "#define USE_XMAX_PLUG"+ Modified), end='')  # Enabling X-Max Endstop
        else : 
            config.set('Configuration.h', 'use_xmax_plug', "off")

        if self.UseYMaxPlug.isChecked() == True :
            config.set('Configuration.h', 'use_ymax_plug', "on")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define USE_YMAX_PLUG", "#define USE_YMAX_PLUG"+ Modified), end='')  # Enabling Y-Max Endstop
        else : 
            config.set('Configuration.h', 'use_ymax_plug', "off")

        if self.UseZMaxPlug.isChecked() == True :
            config.set('Configuration.h', 'use_zmax_plug', "on")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define USE_ZMAX_PLUG", "#define USE_ZMAX_PLUG"+ Modified), end='')  # Enabling Z-Max Endstop
        else : 
            config.set('Configuration.h', 'use_zmax_plug', "off")

        if self.InvertXMinEndstop.isChecked() == True :
            config.set('Configuration.h', 'xmin_endstop_invert', "false")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("#define X_MIN_ENDSTOP_INVERTING", "#define X_MIN_ENDSTOP_INVERTING true"+ Modified), end='')  # Invering X-Min Endstop
        else : 
            config.set('Configuration.h', 'xmin_endstop_invert', "true")

        if self.InvertYMinEndstop.isChecked() == True :
            config.set('Configuration.h', 'ymin_endstop_invert', "true")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("#define Y_MIN_ENDSTOP_INVERTING", "#define Y_MIN_ENDSTOP_INVERTING true"+ Modified), end='')  # Invering Y-Min Endstop
        else : 
            config.set('Configuration.h', 'ymin_endstop_invert', "flase")

        if self.InvertZMinEndstop.isChecked() == True :
            config.set('Configuration.h', 'zmin_endstop_invert', "true")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("#define Z_MIN_ENDSTOP_INVERTING", "#define Z_MIN_ENDSTOP_INVERTING true"+ Modified), end='')  # Invering Z-Min Endstop
        else : 
            config.set('Configuration.h', 'zmin_endstop_invert', "flase")

        if self.InvertXMaxEndstop.isChecked() == True :
            config.set('Configuration.h', 'xmax_endstop_invert', "true")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("#define X_MAX_ENDSTOP_INVERTING", "#define X_MAX_ENDSTOP_INVERTING true"+ Modified), end='')  # Invering X-Max Endstop
        else : 
            config.set('Configuration.h', 'xmax_endstop_invert', "flase")

        if self.InvertYMaxEndstop.isChecked() == True :
            config.set('Configuration.h', 'ymax_endstop_invert', "true")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("#define Y_MAX_ENDSTOP_INVERTING", "#define Y_MAX_ENDSTOP_INVERTING true"+ Modified), end='')  # Invering Y-Max Endstop
        else : 
            config.set('Configuration.h', 'ymax_endstop_invert', "flase")

        if self.InvertZMaxEndstop.isChecked() == True :
            config.set('Configuration.h', 'zmax_endstop_invert', "true")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("#define Z_MAX_ENDSTOP_INVERTING", "#define Z_MAX_ENDSTOP_INVERTING true"+ Modified), end='')  # Invering Z-Max Endstop
        else : 
            config.set('Configuration.h', 'zmax_endstop_invert', "flase")


        if self.InvertProbeEndstop.isChecked() == True :
            config.set('Configuration.h', 'zprobe_invert', "true")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("#define Z_MIN_PROBE_ENDSTOP_INVERTING", "#define Z_MIN_PROBE_ENDSTOP_INVERTING true"+ Modified), end='')  # Invering Z-Min Probe Endstop
        else : 
            config.set('Configuration.h', 'zprobe_invert', "flase")



        # Steps per Unit ~~~~~~~~~~~
        with fileinput.FileInput(ConfigFile, inplace=True) as file:
            XStepsS = self.XSteps.text()  
            YStepsS = self.YSteps.text()  
            ZStepsS = self.ZSteps.text()
            E0StepsS = self.E0Steps.text()
            config.set('Configuration.h', 'xsteps_per_unit', XStepsS)
            config.set('Configuration.h', 'ysteps_per_unit', YStepsS)
            config.set('Configuration.h', 'zsteps_per_unit', ZStepsS)
            config.set('Configuration.h', 'e0steps_per_unit', E0StepsS)
            NewAllSteps = "#define DEFAULT_AXIS_STEPS_PER_UNIT   { " + XStepsS +", " + YStepsS + ", " + ZStepsS + ", " + E0StepsS + " }"
            #print(NewAllSteps)
            for line in file:
                print(line.replace("#define DEFAULT_AXIS_STEPS_PER_UNIT ", NewAllSteps + Modified ), end='')  # Modifying Default Steps for Unit
        
        # Max Feedrate ~~~~~~~~~~~
        with fileinput.FileInput(ConfigFile, inplace=True) as file:
            XMaxFeRate = self.XMaxFeedRate.text()  
            YMaxFeRate = self.YMaxFeedRate.text()  
            ZMaxFeRate = self.ZMaxFeedRate.text()
            E0MaxFeRate = self.E0MaxFeedRate.text()
            config.set('Configuration.h', 'x_max_feedrate', XMaxFeRate)
            config.set('Configuration.h', 'y_max_feedrate', YMaxFeRate)
            config.set('Configuration.h', 'z_max_feedrate', ZMaxFeRate)
            config.set('Configuration.h', 'e0_max_feedrate', E0MaxFeRate)
            NewAllFerate = "#define DEFAULT_MAX_FEEDRATE   { " + XMaxFeRate +", " + YMaxFeRate + ", " + ZMaxFeRate + ", " + E0MaxFeRate + " }"
            for line in file:
                print(line.replace("#define DEFAULT_MAX_FEEDRATE        ", NewAllFerate + Modified ), end='')  # Modifying Default Feedrate

        # Max Acceleration ~~~~~~~~~~~
        with fileinput.FileInput(ConfigFile, inplace=True) as file:
            XMaxAcc = self.XMaxAccleration.text()  
            YMaxAcc = self.YMaxAccleration.text()  
            ZMaxAcc = self.ZMaxAccleration.text()
            E0MaxAcc = self.E0MaxAccleration.text()
            config.set('Configuration.h', 'x_max_acceleration', XMaxAcc)
            config.set('Configuration.h', 'y_max_acceleration', YMaxAcc)
            config.set('Configuration.h', 'z_max_acceleration', ZMaxAcc)
            config.set('Configuration.h', 'e0_max_acceleration', E0MaxAcc)
            NewAllAcc = "#define DEFAULT_MAX_ACCELERATION   { " + XMaxAcc +", " + YMaxAcc + ", " + ZMaxAcc + ", " + E0MaxAcc + " }"
            for line in file:
                print(line.replace("#define DEFAULT_MAX_ACCELERATION        ", NewAllAcc + Modified ), end='')  # Modifying Default Max Acceleration

        # Z-Probe Options ~~~~~~~~~~~
        if self.UseProbeZHome.isChecked() == True :
            config.set('Configuration.h', 'use_probe_for_z_homing', "on")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("//#define USE_PROBE_FOR_Z_HOMING", "#define USE_PROBE_FOR_Z_HOMING" + Modified), end='')  # Enabling USE_PROBE_FOR_Z_HOMING
        else :
            config.set('Configuration.h', 'use_probe_for_z_homing', "off")

        if self.FixedProbe.isChecked() == True :
            config.set('Configuration.h', 'use_fixed_mounted_probe', "on")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("//#define FIX_MOUNTED_PROBE", "#define FIX_MOUNTED_PROBE" + Modified), end='')  # Enabling FIX_MOUNTED_PROBE
        else :
            config.set('Configuration.h', 'use_fixed_mounted_probe', "off")

        if self.NozzleasProbe.isChecked() == True :
            config.set('Configuration.h', 'use_nozzle_as_probe', "on")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("//#define NOZZLE_AS_PROBE", "#define NOZZLE_AS_PROBE" + Modified), end='')  # Enabling NOZZLE_AS_PROBE
        else :
            config.set('Configuration.h', 'use_nozzle_as_probe', "off")

        if self.BLTtouch.isChecked() == True :
            config.set('Configuration.h', 'use_bltouch', "on")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("//#define BLTOUCH", "#define BLTOUCH" + Modified), end='')  # Enabling BLTOUCH
        else :
            config.set('Configuration.h', 'use_bltouch', "off")

        X_Offset = self.ProbeXOffset.text()  
        Y_Offset = self.ProbeYOffset.text()  
        Z_Offset = self.ProbeZOffset.text()
        config.set('Configuration.h', 'probe_x_offset', X_Offset)
        config.set('Configuration.h', 'probe_y_offset', Y_Offset)
        config.set('Configuration.h', 'probe_z_offset', Z_Offset)
        New_Offsets = "#define NOZZLE_TO_PROBE_OFFSET   { " + X_Offset +", " + Y_Offset + ", " + Z_Offset + " }"
        with fileinput.FileInput(ConfigFile, inplace=True) as file: 
            for line in file:
                print(line.replace("#define NOZZLE_TO_PROBE_OFFSET ", New_Offsets + Modified), end='')  # Changing Z Probe Offsets

        config.set('Configuration.h', 'probing_margin', self.ProbeMargin.text())
        if int(self.ProbeMargin.text()) != 10 :
            NewProbe_Margin = "#define PROBING_MARGIN "+ self.ProbeMargin.text()
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("#define PROBING_MARGIN ", NewProbe_Margin + Modified), end='')  #  Changing PROBING_MARGIN

        if self.MultipleProbing.isChecked() == True :
            config.set('Configuration.h', 'use_multiple_probing', "on")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("//#define MULTIPLE_PROBING 2", "#define MULTIPLE_PROBING 2" + Modified), end='')  # Enabling MULTIPLE_PROBING
        else :
            config.set('Configuration.h', 'use_multiple_probing', "off")

        if self.ExtraProbing.isChecked() == True :
            config.set('Configuration.h', 'use_extra_probing', "on")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("//#define EXTRA_PROBING    1", "#define EXTRA_PROBING    1" + Modified), end='')  # Enabling EXTRA_PROBING
        else :
            config.set('Configuration.h', 'use_extra_probing', "off")

        if self.ProbeHeatOff.isChecked() == True :
            config.set('Configuration.h', 'use_probing_heaters_off', "on")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("//#define PROBING_HEATERS_OFF", "#define PROBING_HEATERS_OFF" + Modified), end='')  # Enabling PROBING_HEATERS_OFF
        else :
            config.set('Configuration.h', 'use_probing_heaters_off', "off")

        if self.PreHeatHoming.isChecked() == True :
            config.set('Configuration.h', 'use_preheat_before_home', "on")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("//#define PREHEAT_BEFORE_PROBING", "#define PREHEAT_BEFORE_PROBING" + Modified), end='')  # Enabling PREHEAT_BEFORE_PROBING
        else :
            config.set('Configuration.h', 'use_preheat_before_home', "off")
        
        # Invert Axis Roation ~~~~~~~~~~~
        if self.InvertXAxis.currentText() != "false" :
            config.set('Configuration.h', 'invert_x_dir', "true")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("#define INVERT_X_DIR ", "#define INVERT_X_DIR true" + Modified), end='')  # Inverting X-Axis Rotation
        else :
            config.set('Configuration.h', 'invert_x_dir', "false")

        if self.InvertYAxis.currentText() != "true" :
            config.set('Configuration.h', 'invert_y_dir', "false")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("#define INVERT_Y_DIR ", "#define INVERT_Y_DIR false" + Modified), end='')  # Inverting Y-Axis Rotation
        else :
            config.set('Configuration.h', 'invert_y_dir', "true")


        if self.InvertZAxis.currentText() != "false" :
            config.set('Configuration.h', 'invert_z_dir', "true")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("#define INVERT_Z_DIR ", "#define INVERT_Z_DIR true" + Modified), end='')  # Inverting Z-Axis Rotation
        else :
            config.set('Configuration.h', 'invert_z_dir', "false")

        if self.InvertE0Axis.currentText() != "false" :
            config.set('Configuration.h', 'invert_e0_dir', "true")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("#define INVERT_E0_DIR ", "#define INVERT_E0_DIR true" + Modified), end='')  # Inverting Z-Axis Rotation
        else :
            config.set('Configuration.h', 'invert_e0_dir', "false")


        # Changing Homing Directtion ~~~~~~~~~~~
        if self.XHoming.currentText() != "min" :
            config.set('Configuration.h', 'x_homing_position', "max")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("#define X_HOME_DIR ", "#define X_HOME_DIR 1" + Modified), end='')  # Changing X-Axis Homing Directtion to Max
        else :
            config.set('Configuration.h', 'x_homing_position', "min")


        if self.YHoming.currentText() != "min" :
            config.set('Configuration.h', 'y_homing_position', "max")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("#define Y_HOME_DIR ", "#define Y_HOME_DIR 1" + Modified), end='')  # Changing Y-Axis Homing Directtion to Max
        else :
            config.set('Configuration.h', 'y_homing_position', "min")


        if self.ZHoming.currentText() != "min" :
            config.set('Configuration.h', 'z_homing_position', "max")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("#define Z_HOME_DIR ", "#define Z_HOME_DIR 1" + Modified), end='')  # Changing Z-Axis Homing Directtion to Max
        else :
            config.set('Configuration.h', 'z_homing_position', "min")


        # Changing Bed Size ~~~~~~~~~~~
        config.set('Configuration.h', 'x_bed_size', self.XBedSize.text())
        if self.XBedSize.text() != "200" :
            NewXBedSize = "#define X_BED_SIZE "+ self.XBedSize.text()
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("#define X_BED_SIZE ", NewXBedSize + Modified), end='')  # Changing X Bed Size

        config.set('Configuration.h', 'y_bed_size', self.YBedSize.text())
        if self.YBedSize.text() != "200" :
            NewYBedSize = "#define Y_BED_SIZE "+ self.YBedSize.text()
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("#define Y_BED_SIZE ", NewYBedSize + Modified), end='')  # Changing Y Bed Size

        config.set('Configuration.h', 'z_height', self.ZHeight.text())
        if self.ZHeight.text() != "200" :
            NewZHeight = "#define Z_MAX_POS "+ self.ZHeight.text()
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("#define Z_MAX_POS ", NewZHeight + Modified), end='')  # Changing Z Height

        config.set('Configuration.h', 'x_min_position', self.XMinPosittion.text())
        if self.XMinPosittion.text() != 0 :
            NewXMinPosition = "#define X_MIN_POS "+ self.XMinPosittion.text()
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("#define X_MIN_POS ", NewXMinPosition + Modified), end='')  # Changing Z Height

        config.set('Configuration.h', 'y_min_position', self.YMinPosittion.text())
        if self.YMinPosittion.text() != 0 :
            NewYMinPosition = "#define Y_MIN_POS "+ self.YMinPosittion.text()
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("#define Y_MIN_POS ", NewYMinPosition + Modified), end='')  # Changing Z Height


        # Filament Sensor ~~~~~~~~~~~~~
        if self.FilamentSensor.isChecked() == True :
            config.set('Configuration.h', 'use_filament_sensor', "on")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("//#define FILAMENT_RUNOUT_SENSOR", "#define FILAMENT_RUNOUT_SENSOR" + Modified), end='')  # Enabling FILAMENT_RUNOUT_SENSOR
        else : 
            config.set('Configuration.h', 'use_filament_sensor', "off")


        if self.FiSenState.currentText() != "LOW" :
            config.set('Configuration.h', 'filament_sensor_state', "high")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("#define FIL_RUNOUT_STATE ",   "#define FIL_RUNOUT_STATE     HIGH" + Modified), end='')  # Changing FIL_RUNOUT_STATE       
        else : 
            config.set('Configuration.h', 'filament_sensor_state', "low")




        # Bed Levelling  ~~~~~~~~~~~~~
        if self.Level3Point.isChecked() == True :
            config.set('Configuration.h', 'leveling_3point', "on")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("//#define AUTO_BED_LEVELING_3POINT", "#define AUTO_BED_LEVELING_3POINT" + Modified), end='')  # Enabling AUTO_BED_LEVELING_3POINT
        else : 
            config.set('Configuration.h', 'leveling_3point', "off")


        if self.Linear.isChecked() == True :
            config.set('Configuration.h', 'leveling_linear', "on")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("//#define AUTO_BED_LEVELING_LINEAR", "#define AUTO_BED_LEVELING_LINEAR" + Modified), end='')  # Enabling AUTO_BED_LEVELING_LINEAR
        else :
            config.set('Configuration.h', 'leveling_linear', "off")


        if self.BiLinear.isChecked() == True :
            config.set('Configuration.h', 'leveling_bilinear', "on")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("//#define AUTO_BED_LEVELING_BILINEAR", "#define AUTO_BED_LEVELING_BILINEAR" + Modified), end='')  # Enabling AUTO_BED_LEVELING_BILINEAR
        else :
            config.set('Configuration.h', 'leveling_bilinear', "off")

        config.set('Configuration.h', 'linear_points', self.LinearPoints.text())
        if self.LinearPoints.text() != "3" :
            NewLiPoints =   "#define GRID_MAX_POINTS_X  " + self.LinearPoints.text()
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("#define GRID_MAX_POINTS_X", NewLiPoints + Modified), end='')  # Changing Grid points for Linear 

        if self.UBL.isChecked() == True :
            config.set('Configuration.h', 'leveling_ubl', "on")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("//#define AUTO_BED_LEVELING_UBL", "#define AUTO_BED_LEVELING_UBL" + Modified), end='')  # Enabling AUTO_BED_LEVELING_UBL
        else : 
            config.set('Configuration.h', 'leveling_ubl', "off")

        config.set('Configuration.h', 'ubl_points', self.UBLLevelPoints.text())
        if self.UBLLevelPoints.text() != "10" :
            NewUBLPoints =   "#define GRID_MAX_POINTS_X " + self.UBLLevelPoints.text()
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("#define GRID_MAX_POINTS_X", NewUBLPoints + Modified), end='')  # Changing Grid points for UBL 

        if self.MeshBed.isChecked() == True :
            config.set('Configuration.h', 'leveling_mesh', "on")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("//#define MESH_BED_LEVELING", "#define MESH_BED_LEVELING" + Modified), end='')  # Enabling MESH_BED_LEVELING
        else : 
            config.set('Configuration.h', 'leveling_mesh', "off")


        if self.RestoreAfterG28.isChecked() == True :
            config.set('Configuration.h', 'restore_after_g28', "on")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("//#define RESTORE_LEVELING_AFTER_G28", "#define RESTORE_LEVELING_AFTER_G28" + Modified), end='')  # Enabling RESTORE_LEVELING_AFTER_G28
        else :
            config.set('Configuration.h', 'restore_after_g28', "off")


        if self.PreHeatLevel.isChecked() == True :
            config.set('Configuration.h', 'preheat_before_level', "on")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("//#define PREHEAT_BEFORE_LEVELING", "#define PREHEAT_BEFORE_LEVELING" + Modified), end='')  # Enabling PREHEAT_BEFORE_LEVELING
        else :
            config.set('Configuration.h', 'preheat_before_level', "off")       


        if self.G26MeshValid.isChecked() == True :
            config.set('Configuration.h', 'g26_mesh_validation', "on")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("//#define G26_MESH_VALIDATION", "  #define G26_MESH_VALIDATION" + Modified), end='')  # Enabling G26_MESH_VALIDATION
        else :
            config.set('Configuration.h', 'g26_mesh_validation', "off")


        if self.ZSafeHome.isChecked() == True :
            config.set('Configuration.h', 'use_z_safe_homing', "on")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("//#define Z_SAFE_HOMING", "#define Z_SAFE_HOMING" + Modified), end='')  # Enabling Z_SAFE_HOMING
        else :
            config.set('Configuration.h', 'use_z_safe_homing', "off")



        # Additional Options ~~~~~~~~~~~~~~~~~~~
        if self.EnableEeprom.isChecked() == True :
            config.set('Configuration.h', 'enable_eeprom', "on")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("//#define EEPROM_SETTINGS", "#define EEPROM_SETTINGS" + Modified), end='')  # Enabling EEPROM_SETTINGS
        else :
            config.set('Configuration.h', 'enable_eeprom', "off") 


        if self.EepromReset.isChecked() == True :
            config.set('Configuration.h', 'reset_on_errors', "on")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("//#define EEPROM_AUTO_INIT", "#define EEPROM_AUTO_INIT" + Modified), end='')  # Enabling EEPROM_AUTO_INIT
        else :
            config.set('Configuration.h', 'reset_on_errors', "off")


        if self.EepromClear.isChecked() == True :
            config.set('Configuration.h', 'clear_old_values', "on")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("//#define EEPROM_INIT_NOW", "#define EEPROM_INIT_NOW" + Modified), end='')  # Enabling EEPROM_INIT_NOW
        else :
            config.set('Configuration.h', 'clear_old_values', "off")


        if self.NozParkFeature.isChecked() == True :
            config.set('Configuration.h', 'nozzle_park_feature', "on")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("//#define NOZZLE_PARK_FEATURE", "#define NOZZLE_PARK_FEATURE" + Modified), end='')  # Enabling NOZZLE_PARK_FEATURE
        else :
            config.set('Configuration.h', 'nozzle_park_feature', "off")


        if self.NozCleanFeature.isChecked() == True :
            config.set('Configuration.h', 'nozzle_clean_feature', "on")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("//#define NOZZLE_CLEAN_FEATURE", "#define NOZZLE_CLEAN_FEATURE" + Modified), end='')  # Enabling NOZZLE_CLEAN_FEATURE
        else :
            config.set('Configuration.h', 'nozzle_clean_feature', "off")


        if self.PrintCounter.isChecked() == True :
            config.set('Configuration.h', 'use_print_counter', "on")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("//#define PRINTCOUNTER", "#define PRINTCOUNTER" + Modified), end='')  # Enabling PRINTCOUNTER
        else :
            config.set('Configuration.h', 'use_print_counter', "off")


        if self.SDSupport.isChecked() == True :
            config.set('Configuration.h', 'use_sd_support', "on")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("//#define SDSUPPORT", "#define SDSUPPORT" + Modified), end='')  # Enabling SDSUPPORT
        else :
            config.set('Configuration.h', 'use_sd_support', "off")


        if self.InAxisHoMenu.isChecked() == True :
            config.set('Configuration.h', 'individial_home_menu', "on")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("//#define INDIVIDUAL_AXIS_HOMING_MENU", "#define INDIVIDUAL_AXIS_HOMING_MENU" + Modified), end='')  # Enabling INDIVIDUAL_AXIS_HOMING_MENU
        else :
            config.set('Configuration.h', 'individial_home_menu', "off")


        if self.Speaker.isChecked() == True :
            config.set('Configuration.h', 'use_speaker', "on")
            with fileinput.FileInput(ConfigFile, inplace=True) as file:
                for line in file:
                    print(line.replace("//#define SPEAKER", "#define SPEAKER" + Modified), end='')  # Enabling SPEAKER
        else : 
            config.set('Configuration.h', 'use_speaker', "off")

        # Displays ~~~~~~~~~~~~~~~~~~~
        NewDisplay = (''.join(self.Display.currentText())) #Get Current text in Displays Combobox'
        NewDisplay = (''.join(NewDisplay.splitlines()))    #To Delete next line '\n'
        config.set('Configuration.h', 'display_type', NewDisplay)
        if NewDisplay == "REPRAP_DISCOUNT_FULL_GRAPHIC_SMART_CONTROLLER" :
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define REPRAP_DISCOUNT_FULL_GRAPHIC_SMART_CONTROLLER", "#define REPRAP_DISCOUNT_FULL_GRAPHIC_SMART_CONTROLLER" + Modified), end='')  # Changing Display

        if NewDisplay == "MKS_TS35_V2_0" :
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define MKS_TS35_V2_0", "#define MKS_TS35_V2_0" + Modified), end='')  # Changing Display

        if NewDisplay == "MKS_ROBIN_TFT24" :
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define MKS_ROBIN_TFT24", "#define MKS_ROBIN_TFT24" + Modified), end='')  # Changing Display

        if NewDisplay == "MKS_ROBIN_TFT28" :
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define MKS_ROBIN_TFT28", "#define MKS_ROBIN_TFT28" + Modified), end='')  # Changing Display

        if NewDisplay == "MKS_ROBIN_TFT32" :
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define MKS_ROBIN_TFT32", "#define MKS_ROBIN_TFT32" + Modified), end='')  # Changing Display
        
        if NewDisplay == "MKS_ROBIN_TFT35" :
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define MKS_ROBIN_TFT35", "#define MKS_ROBIN_TFT35" + Modified), end='')  # Changing Display

        if NewDisplay == "MKS_ROBIN_TFT43" :
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define MKS_ROBIN_TFT43", "#define MKS_ROBIN_TFT43" + Modified), end='')  # Changing Display

        if NewDisplay == "MKS_ROBIN_TFT_V1_1R" :
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define MKS_ROBIN_TFT_V1_1R", "#define MKS_ROBIN_TFT_V1_1R" + Modified), end='')  # Changing Display

        if NewDisplay == "TFT_TRONXY_X5SA" :
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define TFT_TRONXY_X5SA", "#define TFT_TRONXY_X5SA" + Modified), end='')  # Changing Display

        if NewDisplay == "ANYCUBIC_TFT35" :
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define ANYCUBIC_TFT35", "#define ANYCUBIC_TFT35"), end='')  # Changing Display

        if NewDisplay == "LONGER_LK_TFT28" :
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define LONGER_LK_TFT28", "#define LONGER_LK_TFT28" + Modified), end='')  # Changing Display

        if NewDisplay == "ANET_ET4_TFT28" :
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define ANET_ET4_TFT28", "#define ANET_ET4_TFT28" + Modified), end='')  # Changing Display

        if NewDisplay == "ANET_ET5_TFT35" :
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define ANET_ET5_TFT35", "#define ANET_ET5_TFT35" + Modified), end='')  # Changing Display

        if NewDisplay == "BIQU_BX_TFT70" :
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define BIQU_BX_TFT70", "#define BIQU_BX_TFT70" + Modified), end='')  # Changing Display

        if NewDisplay == "BTT_TFT35_SPI_V1_0" :
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define BTT_TFT35_SPI_V1_0", "#define BTT_TFT35_SPI_V1_0" + Modified), end='')  # Changing Display

        if NewDisplay == "DWIN_CREALITY_LCD" :
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define DWIN_CREALITY_LCD", "#define DWIN_CREALITY_LCD" + Modified), end='')  # Changing Display

        if NewDisplay == "DWIN_LCD_PROUI" :
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define DWIN_LCD_PROUI", "#define DWIN_LCD_PROUI" + Modified), end='')  # Changing Display

        if NewDisplay == "DWIN_CREALITY_LCD_JYERSUI" :
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define DWIN_CREALITY_LCD_JYERSUI", "#define DWIN_CREALITY_LCD_JYERSUI" + Modified), end='')  # Changing Display

        if NewDisplay == "DWIN_MARLINUI_PORTRAIT" :
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define DWIN_MARLINUI_PORTRAIT", "#define DWIN_MARLINUI_PORTRAIT" + Modified), end='')  # Changing Display

        if NewDisplay == "DWIN_MARLINUI_LANDSCAPE" :
            with fileinput.FileInput(ConfigFile, inplace=True) as file:   
                for line in file:
                    print(line.replace("//#define DWIN_MARLINUI_LANDSCAPE", "#define DWIN_MARLINUI_LANDSCAPE" + Modified), end='')  # Changing Display




        NewPrinterType= (''.join(self.PrinterType.currentText())) 
        NewPrinterType = (''.join(NewPrinterType.splitlines()))    #To Delete next line '\n' 
        config.set('Configuration.h', 'printer_type', NewPrinterType)
        if NewPrinterType == "COREXY" :
            with fileinput.FileInput(ConfigFile, inplace=True, errors='ignore') as file:  
                for line in file:
                    print(line.replace("//#define COREXY", "#define COREXY" + Modified), end='')  # Enabling COREXY

        if NewPrinterType == "COREXZ" :
            with fileinput.FileInput(ConfigFile, inplace=True, errors='ignore') as file:  
                for line in file:
                    print(line.replace("//#define COREXZ", "#define COREXZ" + Modified), end='')  # Enabling COREXZ

        if NewPrinterType == "COREYZ" :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as file:  
                for line in file:
                    print(line.replace("//#define COREYZ", "#define COREYZ" + Modified), end='')  # Enabling COREYZ

        if NewPrinterType == "COREYX" :
            with fileinput.FileInput(ConfigFile, inplace=True, errors='ignore') as file:  
                for line in file:
                    print(line.replace("//#define COREYX", "#define COREYX" + Modified), end='')  # Enabling COREYX

        if NewPrinterType == "COREZX" :
            with fileinput.FileInput(ConfigFile, inplace=True, errors='ignore') as file:  
                for line in file:
                    print(line.replace("//#define COREZX", "#define COREZX" + Modified), end='')  # Enabling COREZX

        if NewPrinterType == "COREZY" :
            with fileinput.FileInput(ConfigFile, inplace=True, errors='ignore') as file:  
                for line in file:
                    print(line.replace("//#define COREZY", "#define COREZY" + Modified), end='')  # Enabling COREZY

        if NewPrinterType == "MARKFORGED_XY" :
            with fileinput.FileInput(ConfigFile, inplace=True, errors='ignore') as file:  
                for line in file:
                    print(line.replace("//#define MARKFORGED_XY", "#define MARKFORGED_XY" + Modified), end='')  # Enabling MARKFORGED_XY

        if NewPrinterType == "MARKFORGED_YX" :
            with fileinput.FileInput(ConfigFile, inplace=True, errors='ignore') as file:  
                for line in file:
                    print(line.replace("//#define MARKFORGED_YX", "#define MARKFORGED_YX" + Modified), end='')  # Enabling MARKFORGED_YX

        if NewPrinterType == "BELTPRINTER" :
            with fileinput.FileInput(ConfigFile, inplace=True, errors='ignore') as file:  
                for line in file:
                    print(line.replace("//#define BELTPRINTER", "#define BELTPRINTER" + Modified), end='')  # Enabling BELTPRINTER

        #~~~~~~~~~~~~~~~~~~~~~~ End Changing in Configuration.h File ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~








        #~~~~~~~~~~~~~~~~~~~~~~ Sart Changing in Configuration_adv.h File ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        OrgConfigAdv = SourceDir+'\Configuration_adv.h'
        NewConfigAdv = TargetDir+'\Configuration_adv.h'
        shutil.copy(OrgConfigAdv, NewConfigAdv)   # Copy file to Target Directory efollow_symlinks=True

        if self.ExRunoutPrevent.isChecked() == True :
            config.set('Configuration_adv.h', 'extruder_runout_prevent', "on")
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:   
                for line in advfile:
                    print(line.replace("//#define EXTRUDER_RUNOUT_PREVENT", "#define EXTRUDER_RUNOUT_PREVENT" + Modified), end='')  # Enabling EXTRUDER_RUNOUT_PREVENT
        else :
            config.set('Configuration_adv.h', 'extruder_runout_prevent', "off")


        if self.UseConrollerFan.isChecked() == True :
            config.set('Configuration_adv.h', 'use_controller_fan', "on")
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("//#define USE_CONTROLLER_FAN", "#define USE_CONTROLLER_FAN" + Modified), end='')  # Enabling USE_CONTROLLER_FAN
        else :
            config.set('Configuration_adv.h', 'use_controller_fan', "off")


        if self.FastPWMFan.isChecked() == True :
            config.set('Configuration_adv.h', 'fast_pwm_fan', "on")
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("//#define FAST_PWM_FAN ", "#define FAST_PWM_FAN" + Modified), end='')  # Enabling FAST_PWM_FAN
        else :
            config.set('Configuration_adv.h', 'fast_pwm_fan', "off")

        config.set('Configuration_adv.h', 'extruder_auto_fan_temp', self.ExAutoFanTemp.text())
        if int(self.ExAutoFanTemp.text()) != 50 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define EXTRUDER_AUTO_FAN_TEMPERATURE ", "#define EXTRUDER_AUTO_FAN_TEMPERATURE "+self.ExAutoFanTemp.text() + Modified), end='')  # Changing Temparature

        if self.BLTouchHighSpeed.isChecked() == True :
            config.set('Configuration_adv.h', 'use_bltouch_high_speed', "on")
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("//#define BLTOUCH_HS_MODE true", "#define BLTOUCH_HS_MODE true" + Modified), end='')  # Enabling BLTOUCH_HS_MODE
        else :
            config.set('Configuration_adv.h', 'use_bltouch_high_speed', "off")


        if self.ZAutoAlign.isChecked() == True :
            config.set('Configuration_adv.h', 'use_z_steppers_auto_align', "on")
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("//#define Z_STEPPER_AUTO_ALIGN", "#define Z_STEPPER_AUTO_ALIGN" + Modified), end='')  # Enabling Z_STEPPER_AUTO_ALIGN
        else :
            config.set('Configuration_adv.h', 'use_z_steppers_auto_align', "off")


        if self.AdStepSmooth.isChecked() == True :
            config.set('Configuration_adv.h', 'use_adaptive_step_smoothing', "on")
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("//#define ADAPTIVE_STEP_SMOOTHING", "#define ADAPTIVE_STEP_SMOOTHING" + Modified), end='')  # Enabling ADAPTIVE_STEP_SMOOTHING
        else :
            config.set('Configuration_adv.h', 'use_adaptive_step_smoothing', "off")


        if self.PowLossRecover.isChecked() == True :
            config.set('Configuration_adv.h', 'use_powerloss_recovery', "on")
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("//#define POWER_LOSS_RECOVERY", "#define POWER_LOSS_RECOVERY" + Modified), end='')  # Enabling POWER_LOSS_RECOVERY
        else :
            config.set('Configuration_adv.h', 'use_powerloss_recovery', "off")


        
        # BabyStepping ~~~~~~~~~~~
        if self.BabyStepping.isChecked() == True :
            config.set('Configuration_adv.h', 'enable_baby_stepping', "on")
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("//#define BABYSTEPPING", "#define BABYSTEPPING" + Modified), end='')  # Enabling BABYSTEPPING
        else :
            config.set('Configuration_adv.h', 'enable_baby_stepping', "off")


        if self.IntiBabyStepping.isChecked() == True :
            config.set('Configuration_adv.h', 'inegrated_baby_stepping', "on")
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("//#define INTEGRATED_BABYSTEPPING", "#define INTEGRATED_BABYSTEPPING" + Modified), end='')  # Enabling INTEGRATED_BABYSTEPPING
        else :
            config.set('Configuration_adv.h', 'inegrated_baby_stepping', "off")


        if self.BabyStepWOHome.isChecked() == True :
            config.set('Configuration_adv.h', 'baby_step_without_homing', "on")
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("//#define BABYSTEP_WITHOUT_HOMING", "#define BABYSTEP_WITHOUT_HOMING" + Modified), end='')  # Enabling BABYSTEP_WITHOUT_HOMING
        else :config.set('Configuration_adv.h', 'baby_step_without_homing', "off")


        if self.BabyStepAlwAvail.isChecked() == True :
            config.set('Configuration_adv.h', 'baby_step_always_available', "on")
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("//#define BABYSTEP_ALWAYS_AVAILABLE", "#define BABYSTEP_ALWAYS_AVAILABLE" + Modified), end='')  # Enabling BABYSTEP_ALWAYS_AVAILABLE
        else :
            config.set('Configuration_adv.h', 'baby_step_always_available', "off")


        if self.BabyStepXY.isChecked() == True :
            config.set('Configuration_adv.h', 'baby_step_on_xy', "on")
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("//#define BABYSTEP_XY", "#define BABYSTEP_XY" + Modified), end='')  # Enabling BABYSTEP_XY
        else : 
            config.set('Configuration_adv.h', 'baby_step_on_xy', "off")



        
        # Linear Advance ~~~~~~~~~~~
        if self.LAAvailable.isChecked() == True :
            config.set('Configuration_adv.h', 'use_linear_advance', "on")
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("//#define LIN_ADVANCE", "#define LIN_ADVANCE" + Modified), end='')  # Enabling LIN_ADVANCE
        else :
            config.set('Configuration_adv.h', 'use_linear_advance', "off")


        config.set('Configuration_adv.h', 'linear_advance_kfactor', self.LA_KFactor.text())
        if self.LA_KFactor.text() != 0.22 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  #encoding='utf-8'
                for line in advfile:
                    print(line.replace("#define ADVANCE_K ", "#define ADVANCE_K "+self.LA_KFactor.text() + Modified), end='')  # LIN_ADVANCE K-Factor


        if self.G29RetryRecover.isChecked() == True :
            config.set('Configuration_adv.h', 'use_g29_retry_recover', "on")
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("//#define G29_RETRY_AND_RECOVER", "#define G29_RETRY_AND_RECOVER" + Modified), end='')  # Enabling G29_RETRY_AND_RECOVER
        else :
            config.set('Configuration_adv.h', 'use_g29_retry_recover', "off")



        
        # Dual X - Carriage ~~~~~~~~~~~
        if self.DualXEnable.isChecked() == True :
            config.set('Configuration_adv.h', 'enable_dual_x_carriage', "on")
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("//#define DUAL_X_CARRIAGE", "#define DUAL_X_CARRIAGE" + Modified), end='')  # Enabling DUAL_X_CARRIAGE
        else :
            config.set('Configuration_adv.h', 'enable_dual_x_carriage', "off")


        config.set('Configuration_adv.h', 'dualx_x2_min_position', self.X2MinPosition.text())
        if (self.DualXEnable.isChecked() == True) & (self.X2MinPosition.text() != 80) :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define X2_MIN_POS", "#define X2_MIN_POS   "+self.X2MinPosition.text() + Modified), end='')  # Changing  X2_MIN_POS
        

        config.set('Configuration_adv.h', 'dualx_x2_max_position', self.X2MaxPosition.text())
        if (self.DualXEnable.isChecked() == True) & (self.X2MaxPosition.text() != 353) :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define X2_MAX_POS", "#define X2_MAX_POS   "+self.X2MaxPosition.text() + Modified), end='')  # Changing  X2_MAX_POS
        

        config.set('Configuration_adv.h', 'dualx_duplication_offset', self.DupliOffset.text())
        if (self.DualXEnable.isChecked() == True) & (self.DupliOffset.text() != 100) :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile: 
                NewXDualOffset =  str("#define DEFAULT_DUPLICATION_X_OFFSET   "+self.DupliOffset.text()+"     //Modified")
                for line in advfile:
                    print(line.replace("#define DEFAULT_DUPLICATION_X_OFFSET", NewXDualOffset), end='')  # Changing  DEFAULT_DUPLICATION_X_OFFSET
        
        

        
        # Input Shapping ~~~~~~~~~~~
        if self.InputShappingX.isChecked() == True :
            config.set('Configuration_adv.h', 'enable_x_input_shapping', "on")
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("//#define INPUT_SHAPING_X", "#define INPUT_SHAPING_X" + Modified), end='')  # Enabling INPUT_SHAPING_X
        else :
            config.set('Configuration_adv.h', 'enable_x_input_shapping', "off")


        config.set('Configuration_adv.h', 'x_input_shapping_frequency', self.XInShapeFreq.text())
        if self.XInShapeFreq.text() != 40 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define SHAPING_FREQ_X ", "#define SHAPING_FREQ_X   "+self.XInShapeFreq.text() + Modified), end='')  # Changing SHAPING_FREQ_X
            

        config.set('Configuration_adv.h', 'x_input_shapping_zeta', self.XInShapeZeta.text())
        if self.XInShapeZeta.text() != str("0.15f") :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define SHAPING_ZETA_X ", "#define SHAPING_ZETA_X   "+self.XInShapeZeta.text() + Modified), end='')  # Changing SHAPING_ZETA_X

        if self.InputShappingY.isChecked() == True :
            config.set('Configuration_adv.h', 'enable_y_input_shapping', "on")
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("//#define INPUT_SHAPING_Y", "#define INPUT_SHAPING_Y" + Modified), end='')  # Enabling INPUT_SHAPING_Y
        else :
            config.set('Configuration_adv.h', 'enable_y_input_shapping', "off")


        config.set('Configuration_adv.h', 'y_input_shapping_frequency', self.YInShapeFreq.text())
        if self.YInShapeFreq.text() != 40 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define SHAPING_FREQ_Y ", "#define SHAPING_FREQ_Y   "+self.YInShapeFreq.text() + Modified), end='')  # Changing SHAPING_FREQ_Y


        config.set('Configuration_adv.h', 'y_input_shapping_zeta', self.YInShapeZeta.text())
        if self.YInShapeZeta.text() != str("0.15f") :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define SHAPING_ZETA_Y ", "#define SHAPING_ZETA_Y   "+self.YInShapeZeta.text() + Modified), end='')  # Changing SHAPING_ZETA_Y



        
        # Additional ~~~~~~~~~~~
        NewTxBufSize= (''.join(self.TXBufferSize.currentText())) #Get Current text in BoardTxt Combobox'
        NewTxBufSize = (''.join(NewTxBufSize.splitlines()))    #To Delete next line '\n' 
        config.set('Configuration_adv.h', 'tx_buffer_size', NewTxBufSize)
        if NewTxBufSize != 0 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define TX_BUFFER_SIZE ", "#define TX_BUFFER_SIZE   "+ NewTxBufSize + Modified), end='')  # Changing TX_BUFFER_SIZE

        if self.EmeParser.isChecked() == True :
            config.set('Configuration_adv.h', 'use_emergency_parcer', "on")
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("//#define EMERGENCY_PARSER", "#define EMERGENCY_PARSER" + Modified), end='')  # Enabling EMERGENCY_PARSER
        else :
            config.set('Configuration_adv.h', 'use_emergency_parcer', "off")


        if self.AdvancedOK.isChecked() == True :
            config.set('Configuration_adv.h', 'use_advanced_ok', "on")
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("//#define ADVANCED_OK", "#define ADVANCED_OK" + Modified), end='')  # Enabling ADVANCED_OK
        else :
            config.set('Configuration_adv.h', 'use_advanced_ok', "off")


        if self.AdvPause.isChecked() == True :
            config.set('Configuration_adv.h', 'advanced_pause_feature', "on")
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("//#define ADVANCED_PAUSE_FEATURE", "#define ADVANCED_PAUSE_FEATURE" + Modified), end='')  # Enabling ADVANCED_PAUSE_FEATURE
        else :
            config.set('Configuration_adv.h', 'advanced_pause_feature', "off")


        if self.MoDriverStatus.isChecked() == True :
            config.set('Configuration_adv.h', 'monitor_driver_status', "on")
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("//#define MONITOR_DRIVER_STATUS", "#define MONITOR_DRIVER_STATUS" + Modified), end='')  # Enabling MONITOR_DRIVER_STATUS
        else :
            config.set('Configuration_adv.h', 'monitor_driver_status', "off")


        NewChoVoltage= (''.join(self.ChoVoltage.currentText())) #Get Current text in BoardTxt Combobox'
        NewChoVoltage = (''.join(NewChoVoltage.splitlines()))    #To Delete next line '\n' 
        config.set('Configuration_adv.h', 'chopper_voltage', NewChoVoltage)
        if NewChoVoltage != "CHOPPER_DEFAULT_12V" :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define CHOPPER_TIMING CHOPPER_DEFAULT_12V", "#define CHOPPER_TIMING "+ NewChoVoltage + Modified), end='')  # Changing Chopper Voltage

        if self.SenLessHome.isChecked() == True :
            config.set('Configuration_adv.h', 'sensorless_homing', "on")
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("//#define SENSORLESS_HOMING", "#define SENSORLESS_HOMING" + Modified), end='')  # Enabling SENSORLESS_HOMING
        else :
            config.set('Configuration_adv.h', 'sensorless_homing', "off")


        if self.TMCDebug.isChecked() == True :
            config.set('Configuration_adv.h', 'use_tmc_debugging', "on")
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("//#define TMC_DEBUG", "#define TMC_DEBUG" + Modified), end='')  # Enabling TMC_DEBUG
        else :
            config.set('Configuration_adv.h', 'use_tmc_debugging', "off")


        if self.LongFileName.isChecked() == True :
            config.set('Configuration_adv.h', 'long_filename_support', "on")
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("//#define LONG_FILENAME_HOST_SUPPORT", "#define LONG_FILENAME_HOST_SUPPORT" + Modified), end='')  # Enabling SCROLL_LONG_FILENAMES
        else :
            config.set('Configuration_adv.h', 'long_filename_support', "off")


        if self.ScrolLongFile.isChecked() == True :
            config.set('Configuration_adv.h', 'scroll_long_filename', "on")
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("//#define SCROLL_LONG_FILENAMES", "#define SCROLL_LONG_FILENAMES" + Modified), end='')  # Enabling SCROLL_LONG_FILENAMES
        else :
            config.set('Configuration_adv.h', 'scroll_long_filename', "off")
        # Current and Microsteps ~~~~~~~~~~~~~  
          
        #config.set('Configuration_adv.h', 'x_current', self.XCurrent.text())
        config.set('Configuration_adv.h', 'x_current', self.XCurrent.text())
        if self.XCurrent.text() != 800 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define X_CURRENT  ", "#define X_CURRENT     "+ self.XCurrent.text() + Modified), end='')  # Changing X_CURRENT

        NewXMicrosteps= (''.join(self.XMicrosteps.currentText())) #Get Current text in BoardTxt Combobox'
        NewXMicrosteps = (''.join(NewXMicrosteps.splitlines()))    #To Delete next line '\n' 
        config.set('Configuration_adv.h', 'x_micro_steps', NewXMicrosteps)
        if NewXMicrosteps != 16 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define X_MICROSTEPS", "#define X_MICROSTEPS       "+ NewXMicrosteps + Modified), end='')  # Changing X_MICROSTEPS

        config.set('Configuration_adv.h', 'x_rense', self.XRence.text())
        if self.XRence.text() != 0.11 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define X_RSENSE", "#define X_RSENSE        "+ self.XRence.text() + Modified), end='')  # Changing X_RSENSE

        config.set('Configuration_adv.h', 'x2_current', self.X2Current.text())
        if self.X2Current.text() != 800 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define X2_CURRENT  ", "#define X2_CURRENT        "+ self.XCurrent.text() + Modified), end='')  # Changing X2_CURRENT

        NewX2Microsteps= (''.join(self.X2Microsteps.currentText())) #Get Current text in BoardTxt Combobox'
        NewX2Microsteps = (''.join(NewX2Microsteps.splitlines()))    #To Delete next line '\n'
        config.set('Configuration_adv.h', 'x2_micro_steps', NewX2Microsteps) 
        if NewX2Microsteps != 16 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define X2_MICROSTEPS", "#define X2_MICROSTEPS      "+ NewX2Microsteps + Modified), end='')  # Changing X2_MICROSTEPS

        config.set('Configuration_adv.h', 'x2_rense', self.X2Rence.text())
        if self.X2Rence.text() != 0.11 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define X2_RSENSE", "#define X2_RSENSE      "+ self.X2Rence.text() + Modified), end='')  # Changing X2_RSENSE

        config.set('Configuration_adv.h', 'y_current', self.YCurrent.text())
        if self.YCurrent.text() != 800 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define Y_CURRENT  ", "#define Y_CURRENT      "+ self.YCurrent.text() + Modified), end='')  # Changing Y_CURRENT

        NewYMicrosteps= (''.join(self.YMicrosteps.currentText())) #Get Current text in BoardTxt Combobox'
        NewYMicrosteps = (''.join(NewYMicrosteps.splitlines()))    #To Delete next line '\n' 
        config.set('Configuration_adv.h', 'y_micro_steps', NewYMicrosteps) 
        if NewYMicrosteps != 16 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define Y_MICROSTEPS", "#define Y_MICROSTEPS     "+ NewYMicrosteps + Modified), end='')  # Changing Y_MICROSTEPS

        config.set('Configuration_adv.h', 'y_rense', self.YRence.text())
        if self.YRence.text() != 0.11 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define Y_RSENSE", "#define Y_RSENSE        "+ self.YRence.text() + Modified), end='')  # Changing Y_RSENSE

        config.set('Configuration_adv.h', 'y2_current', self.Y2Current.text())
        if self.Y2Current.text() != 800 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define Y2_CURRENT  ", "#define Y2_CURRENT        "+ self.Y2Current.text() + Modified), end='')  # Changing Y2_CURRENT

        NewY2Microsteps= (''.join(self.Y2Microsteps.currentText())) 
        NewY2Microsteps = (''.join(NewY2Microsteps.splitlines()))    #To Delete next line '\n' 
        config.set('Configuration_adv.h', 'y2_micro_steps', NewY2Microsteps) 
        if NewY2Microsteps != 16 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define Y2_MICROSTEPS", "#define Y2_MICROSTEPS      "+ NewY2Microsteps + Modified), end='')  # Changing Y2_MICROSTEPS

        config.set('Configuration_adv.h', 'y2_rense', self.Y2Rence.text())
        if self.Y2Rence.text() != 0.11 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define Y2_RSENSE", "#define Y2_RSENSE      "+ self.Y2Rence.text() + Modified), end='')  # Changing Y2_RSENSE

        config.set('Configuration_adv.h', 'z_current', self.ZCurrent.text())
        if self.ZCurrent.text() != 800 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define Z_CURRENT  ", "#define Z_CURRENT      "+ self.ZCurrent.text() + Modified), end='')  # Changing Z_CURRENT

        NewZMicrosteps= (''.join(self.ZMicrosteps.currentText())) 
        NewZMicrosteps = (''.join(NewZMicrosteps.splitlines()))    #To Delete next line '\n' 
        config.set('Configuration_adv.h', 'z_micro_steps', NewZMicrosteps) 
        if NewZMicrosteps != 16 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define Z_MICROSTEPS", "#define Z_MICROSTEPS        "+ NewZMicrosteps + Modified), end='')  # Changing Z_MICROSTEPS

        config.set('Configuration_adv.h', 'z_rense', self.ZRence.text())
        if self.ZRence.text() != 0.11 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define Z_RSENSE", "#define Z_RSENSE        "+ self.ZRence.text() + Modified), end='')  # Changing Z_RSENSE

        config.set('Configuration_adv.h', 'z2_current', self.Z2Current.text())
        if self.Z2Current.text() != 800 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define Z2_CURRENT  ", "#define Z2_CURRENT        "+ self.Z2Current.text() + Modified), end='')  # Changing Z2_CURRENT

        NewZ2Microsteps= (''.join(self.Z2Microsteps.currentText())) 
        NewZ2Microsteps = (''.join(NewZ2Microsteps.splitlines()))    #To Delete next line '\n' 
        config.set('Configuration_adv.h', 'z2_micro_steps', NewZ2Microsteps) 
        if NewZ2Microsteps != 16 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define Z2_MICROSTEPS", "#define Z2_MICROSTEPS      "+ NewZ2Microsteps + Modified), end='')  # Changing Z2_MICROSTEPS

        config.set('Configuration_adv.h', 'z2_rense', self.Z2Rence.text())
        if self.Z2Rence.text() != 0.11 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define Z2_RSENSE", "#define Z2_RSENSE      "+ self.Z2Rence.text() + Modified), end='')  # Changing Z2_RSENSE

        config.set('Configuration_adv.h', 'z3_current', self.Z3Current.text())
        if self.Z3Current.text() != 800 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define Z3_CURRENT  ", "#define Z3_CURRENT        "+ self.Z3Current.text() + Modified), end='')  # Changing Z3_CURRENT

        NewZ3Microsteps= (''.join(self.Z3Microsteps.currentText())) 
        NewZ3Microsteps = (''.join(NewZ3Microsteps.splitlines()))    #To Delete next line '\n' 
        config.set('Configuration_adv.h', 'z3_micro_steps', NewZ3Microsteps) 
        if NewZ3Microsteps != 16 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define Z3_MICROSTEPS", "#define Z3_MICROSTEPS      "+ NewZ3Microsteps + Modified), end='')  # Changing Z3_MICROSTEPS

        config.set('Configuration_adv.h', 'z3_rense', self.Z3Rence.text())
        if self.Z3Rence.text() != 0.11 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define Z3_RSENSE", "#define Z3_RSENSE      "+ self.Z3Rence.text() + Modified), end='')  # Changing Z3_RSENSE            

        config.set('Configuration_adv.h', 'z4_current', self.Z4Current.text())
        if self.Z4Current.text() != 800 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define Z4_CURRENT  ", "#define Z4_CURRENT        "+ self.Z4Current.text() + Modified), end='')  # Changing Z4_CURRENT

        NewZ4Microsteps= (''.join(self.Z4Microsteps.currentText())) 
        NewZ4Microsteps = (''.join(NewZ4Microsteps.splitlines()))    #To Delete next line '\n' 
        config.set('Configuration_adv.h', 'z4_micro_steps', NewZ4Microsteps) 
        if NewZ4Microsteps != 16 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define Z4_MICROSTEPS", "#define Z4_MICROSTEPS      "+ NewZ4Microsteps + Modified), end='')  # Changing Z4_MICROSTEPS

        config.set('Configuration_adv.h', 'z4_rense', self.Z4Rence.text())
        if self.Z4Rence.text() != 0.11 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define Z4_RSENSE", "#define Z4_RSENSE      "+ self.Z4Rence.text() + Modified), end='')  # Changing Z4_RSENSE


        config.set('Configuration_adv.h', 'e0_current', self.E0Current.text())
        if self.E0Current.text() != 800 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define E0_CURRENT  ", "#define E0_CURRENT        "+ self.E0Current.text() + Modified), end='')  # Changing E0_CURRENT

        NewE0Microsteps= (''.join(self.E0Microsteps.currentText())) 
        NewE0Microsteps = (''.join(NewE0Microsteps.splitlines()))    #To Delete next line '\n' 
        config.set('Configuration_adv.h', 'e0_micro_steps', NewE0Microsteps) 
        if NewE0Microsteps != 16 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define E0_MICROSTEPS", "#define E0_MICROSTEPS      "+ NewE0Microsteps + Modified), end='')  # Changing E0_MICROSTEPS

        config.set('Configuration_adv.h', 'e0_rense', self.E0Rence.text())
        if self.E0Rence.text() != 0.11 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define E0_RSENSE", "#define E0_RSENSE       "+ self.E0Rence.text() + Modified), end='')  # Changing E0_RSENSE

        config.set('Configuration_adv.h', 'e1_current', self.E1Current.text())
        if self.E1Current.text() != 800 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define E1_CURRENT  ", "#define E1_CURRENT        "+ self.E1Current.text() + Modified), end='')  # Changing E1_CURRENT

        NewE1Microsteps= (''.join(self.E1Microsteps.currentText())) 
        NewE1Microsteps = (''.join(NewE1Microsteps.splitlines()))    #To Delete next line '\n' 
        config.set('Configuration_adv.h', 'e1_micro_steps', NewE1Microsteps) 
        if NewE1Microsteps != 16 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define E1_MICROSTEPS", "#define E1_MICROSTEPS      "+ NewE1Microsteps + Modified), end='')  # Changing E1_MICROSTEPS

        config.set('Configuration_adv.h', 'e1_rense', self.E1Rence.text())
        if self.E1Rence.text() != 0.11 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define E1_RSENSE", "#define E1_RSENSE      "+ self.E1Rence.text() + Modified), end='')  # Changing E1_RSENSE

        config.set('Configuration_adv.h', 'e2_current', self.E2Current.text())
        if self.E2Current.text() != 800 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define E2_CURRENT  ", "#define E2_CURRENT        "+ self.E2Current.text() + Modified), end='')  # Changing E2_CURRENT

        NewE2Microsteps= (''.join(self.E2Microsteps.currentText())) 
        NewE2Microsteps = (''.join(NewE2Microsteps.splitlines()))    #To Delete next line '\n' 
        config.set('Configuration_adv.h', 'e2_micro_steps', NewE2Microsteps) 
        if NewE2Microsteps != 16 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define E2_MICROSTEPS", "#define E2_MICROSTEPS      "+ NewE2Microsteps + Modified), end='')  # Changing E2_MICROSTEPS

        config.set('Configuration_adv.h', 'e2_rense', self.E2Rence.text())
        if self.E2Rence.text() != 0.11 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define E2_RSENSE", "#define E2_RSENSE      "+ self.E2Rence.text() + Modified), end='')  # Changing E2_RSENSE

        config.set('Configuration_adv.h', 'e3_current', self.E3Current.text())
        if self.E3Current.text() != 800 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define E3_CURRENT  ", "#define E3_CURRENT        "+ self.E3Current.text() + Modified), end='')  # Changing E3_CURRENT

        NewE3Microsteps= (''.join(self.E2Microsteps.currentText())) 
        NewE3Microsteps = (''.join(NewE3Microsteps.splitlines()))    #To Delete next line '\n' 
        config.set('Configuration_adv.h', 'e3_micro_steps', NewE3Microsteps) 
        if NewE3Microsteps != 16 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define E3_MICROSTEPS", "#define E3_MICROSTEPS      "+ NewE3Microsteps + Modified), end='')  # Changing E3_MICROSTEPS

        config.set('Configuration_adv.h', 'e3_rense', self.E3Rence.text())
        if self.E3Rence.text() != 0.11 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define E3_RSENSE", "#define E3_RSENSE      "+ self.E3Rence.text() + Modified), end='')  # Changing E3_RSENSE

        config.set('Configuration_adv.h', 'e4_current', self.E4Current.text())
        if self.E4Current.text() != 800 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define E4_CURRENT  ", "#define E4_CURRENT        "+ self.E4Current.text() + Modified), end='')  # Changing E4_CURRENT

        NewE4Microsteps= (''.join(self.E4Microsteps.currentText())) 
        NewE4Microsteps = (''.join(NewE4Microsteps.splitlines()))    #To Delete next line '\n' 
        config.set('Configuration_adv.h', 'e4_micro_steps', NewE4Microsteps) 
        if NewE4Microsteps != 16 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define E4_MICROSTEPS", "#define E4_MICROSTEPS      "+ NewE4Microsteps + Modified), end='')  # Changing E4_MICROSTEPS

        config.set('Configuration_adv.h', 'e4_rense', self.E4Rence.text())
        if self.E4Rence.text() != 0.11 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define E4_RSENSE", "#define E4_RSENSE      "+ self.E4Rence.text() + Modified), end='')  # Changing E4_RSENSE

        config.set('Configuration_adv.h', 'e5_current', self.E5Current.text())
        if self.E5Current.text() != 800 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define E5_CURRENT  ", "#define E5_CURRENT        "+ self.E5Current.text() + Modified), end='')  # Changing E5_CURRENT

        NewE5Microsteps= (''.join(self.E5Microsteps.currentText())) 
        NewE5Microsteps = (''.join(NewE5Microsteps.splitlines()))    #To Delete next line '\n' 
        config.set('Configuration_adv.h', 'e5_micro_steps', NewE5Microsteps) 
        if NewE5Microsteps != 16 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define E5_MICROSTEPS", "#define E5_MICROSTEPS      "+ NewE5Microsteps + Modified), end='')  # Changing E5_MICROSTEPS

        config.set('Configuration_adv.h', 'e5_rense', self.E5Rence.text())
        if self.E5Rence.text() != 0.11 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define E5_RSENSE", "#define E5_RSENSE      "+ self.E5Rence.text() + Modified), end='')  # Changing E5_RSENSE

        config.set('Configuration_adv.h', 'e6_current', self.E6Current.text())
        if self.E6Current.text() != 800 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define E6_CURRENT  ", "#define E6_CURRENT        "+ self.E6Current.text() + Modified), end='')  # Changing E6_CURRENT

        NewE6Microsteps= (''.join(self.E6Microsteps.currentText())) 
        NewE6Microsteps = (''.join(NewE6Microsteps.splitlines()))    #To Delete next line '\n' 
        config.set('Configuration_adv.h', 'e6_micro_steps', NewE6Microsteps) 
        if NewE6Microsteps != 16 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define E6_MICROSTEPS", "#define E6_MICROSTEPS      "+ NewE6Microsteps + Modified), end='')  # Changing E6_MICROSTEPS

        config.set('Configuration_adv.h', 'e6_rense', self.E6Rence.text())
        if self.E6Rence.text() != 0.11 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define E6_RSENSE", "#define E6_RSENSE      "+ self.E6Rence.text() + Modified), end='')  # Changing E6_RSENSE

        config.set('Configuration_adv.h', "e7_current", self.E7Current.text())
        if self.E7Current.text() != 800 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define E7_CURRENT  ", "#define E7_CURRENT        "+ self.E7Current.text() + Modified), end='')  # Changing E7_CURRENT

        NewE7Microsteps= (''.join(self.E7Microsteps.currentText())) 
        NewE7Microsteps = (''.join(NewE7Microsteps.splitlines()))    #To Delete next line '\n' 
        config.set('Configuration_adv.h', "e7_micro_steps", NewE7Microsteps) 
        if NewE7Microsteps != 16 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define E7_MICROSTEPS", "#define E7_MICROSTEPS      "+ NewE7Microsteps + Modified), end='')  # Changing E7_MICROSTEPS

        config.set('Configuration_adv.h', 'e7_rense', self.E7Rence.text())
        if self.E7Rence.text() != 0.11 :
            with fileinput.FileInput(NewConfigAdv, inplace=True, errors='ignore') as advfile:  
                for line in advfile:
                    print(line.replace("#define E7_RSENSE", "#define E7_RSENSE      "+ self.E7Rence.text() + Modified), end='')  # Changing E7_RSENSE

        
        with open(configfile, 'w') as newconfigfile:   # Update Config.ini file wih new Values
            config.write(newconfigfile) #space_around_delimiters=True

        self.ShowSuccessMsg()

    def ShowSuccessMsg(self):
        QMessageBox.information(self, "Message", "Configutation Success !!!")

    






    
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
    

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  Start selection of Y Driver comboboxes  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def YMotorsNo_changed(self):
        tot_YDrivers = int(self.YMotorsNo.currentText())

        if tot_YDrivers == 1 : 
            self.Y2_Driver.setEnabled(False)
            self.Y2Current.setEnabled(False)
            self.Y2Microsteps.setEnabled(False)
            self.Y2Rence.setEnabled(False) 
            config.set('Configuration.h', 'y_motors','1')

        elif tot_YDrivers == 2 : 
            self.Y2_Driver.setEnabled(True)
            self.Y2Current.setEnabled(True)
            self.Y2Microsteps.setEnabled(True)
            self.Y2Rence.setEnabled(True)   
            config.set('Configuration.h', 'y_motors','2')  
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  End selection of X Driver comboboxes  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  Start selection of Y Driver comboboxes  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def ZMotorsNo_changed(self):
        tot_ZDrivers = int(self.ZMotorsNo.currentText())        

        if tot_ZDrivers == 1 : 
            self.Z2_Driver.setEnabled(False)
            self.Z3_Driver.setEnabled(False)
            self.Z4_Driver.setEnabled(False)
            self.Z2Current.setEnabled(False)
            self.Z2Microsteps.setEnabled(False)
            self.Z2Rence.setEnabled(False) 
            self.Z3Current.setEnabled(False)
            self.Z3Microsteps.setEnabled(False)
            self.Z3Rence.setEnabled(False)
            self.Z4Current.setEnabled(False)
            self.Z4Microsteps.setEnabled(False)
            self.Z4Rence.setEnabled(False)
            config.set('Configuration.h', 'z_motors','1')

        elif tot_ZDrivers == 2 : 
            self.Z2_Driver.setEnabled(True)
            self.Z3_Driver.setEnabled(False)
            self.Z4_Driver.setEnabled(False) 
            self.Z2Current.setEnabled(True)
            self.Z2Microsteps.setEnabled(True)
            self.Z2Rence.setEnabled(True) 
            self.Z3Current.setEnabled(False)
            self.Z3Microsteps.setEnabled(False)
            self.Z3Rence.setEnabled(False)
            self.Z4Current.setEnabled(False)
            self.Z4Microsteps.setEnabled(False)
            self.Z4Rence.setEnabled(False)
            config.set('Configuration.h', 'z_motors','2')

        elif tot_ZDrivers == 3 : 
            self.Z2_Driver.setEnabled(True)
            self.Z3_Driver.setEnabled(True)
            self.Z4_Driver.setEnabled(False)
            self.Z2Current.setEnabled(True)
            self.Z2Microsteps.setEnabled(True)
            self.Z2Rence.setEnabled(True)
            self.Z3Current.setEnabled(True)
            self.Z3Microsteps.setEnabled(True)
            self.Z3Rence.setEnabled(True) 
            config.set('Configuration.h', 'z_motors','3')  

        elif tot_ZDrivers == 4 : 
            self.Z2_Driver.setEnabled(True)
            self.Z3_Driver.setEnabled(True)
            self.Z4_Driver.setEnabled(True)
            self.Z2Current.setEnabled(True)
            self.Z2Microsteps.setEnabled(True)
            self.Z2Rence.setEnabled(True) 
            self.Z3Current.setEnabled(True)
            self.Z3Microsteps.setEnabled(True)
            self.Z3Rence.setEnabled(True)
            self.Z4Current.setEnabled(True)
            self.Z4Microsteps.setEnabled(True)
            self.Z4Rence.setEnabled(True) 
            config.set('Configuration.h', 'z_motors','4')
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  End selection of X Driver comboboxes  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  Start selection of Extruders Driver comboboxes  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def extruders_changed(self):
        tot_extruders = int(self.Extruders.currentText())
          
        #print(tot_extruders)

        if tot_extruders == 1 : 
                self.E1_Driver.setEnabled(False)
                self.E2_Driver.setEnabled(False)
                self.E2_Driver.setEnabled(False)
                self.E3_Driver.setEnabled(False)
                self.E4_Driver.setEnabled(False)
                self.E5_Driver.setEnabled(False)
                self.E6_Driver.setEnabled(False)
                self.E7_Driver.setEnabled(False)
                self.E1Current.setEnabled(False)
                self.E1Microsteps.setEnabled(False)
                self.E1Rence.setEnabled(False)
                self.E2Current.setEnabled(False)
                self.E2Microsteps.setEnabled(False)
                self.E2Rence.setEnabled(False) 
                self.E3Current.setEnabled(False)
                self.E3Microsteps.setEnabled(False)
                self.E3Rence.setEnabled(False)
                self.E4Current.setEnabled(False)
                self.E4Microsteps.setEnabled(False)
                self.E4Rence.setEnabled(False)
                self.E5Current.setEnabled(False)
                self.E5Microsteps.setEnabled(False)
                self.E5Rence.setEnabled(False)
                self.E6Current.setEnabled(False)
                self.E6Microsteps.setEnabled(False)
                self.E6Rence.setEnabled(False)
                self.E7Current.setEnabled(False)
                self.E7Microsteps.setEnabled(False)
                self.E7Rence.setEnabled(False)
                
        elif tot_extruders == 2 : 
                self.E1_Driver.setEnabled(True)
                self.E2_Driver.setEnabled(False)
                self.E2_Driver.setEnabled(False)
                self.E3_Driver.setEnabled(False)
                self.E4_Driver.setEnabled(False)
                self.E5_Driver.setEnabled(False)
                self.E6_Driver.setEnabled(False)
                self.E7_Driver.setEnabled(False)
                self.E1Current.setEnabled(True)
                self.E1Microsteps.setEnabled(True)
                self.E1Rence.setEnabled(True) 
                self.E2Current.setEnabled(False)
                self.E2Microsteps.setEnabled(False)
                self.E2Rence.setEnabled(False) 
                self.E3Current.setEnabled(False)
                self.E3Microsteps.setEnabled(False)
                self.E3Rence.setEnabled(False)
                self.E4Current.setEnabled(False)
                self.E4Microsteps.setEnabled(False)
                self.E4Rence.setEnabled(False)
                self.E5Current.setEnabled(False)
                self.E5Microsteps.setEnabled(False)
                self.E5Rence.setEnabled(False)
                self.E6Current.setEnabled(False)
                self.E6Microsteps.setEnabled(False)
                self.E6Rence.setEnabled(False)
                self.E7Current.setEnabled(False)
                self.E7Microsteps.setEnabled(False)
                self.E7Rence.setEnabled(False)


        elif tot_extruders == 3 : 
                self.E1_Driver.setEnabled(True) 
                self.E2_Driver.setEnabled(True)
                self.E3_Driver.setEnabled(False)
                self.E4_Driver.setEnabled(False)
                self.E5_Driver.setEnabled(False)
                self.E6_Driver.setEnabled(False)  
                self.E7_Driver.setEnabled(False) 
                self.E1Current.setEnabled(True)
                self.E1Microsteps.setEnabled(True)
                self.E1Rence.setEnabled(True) 
                self.E2Current.setEnabled(True)
                self.E2Microsteps.setEnabled(True)
                self.E2Rence.setEnabled(True) 
                self.E3Current.setEnabled(False)
                self.E3Microsteps.setEnabled(False)
                self.E3Rence.setEnabled(False)
                self.E4Current.setEnabled(False)
                self.E4Microsteps.setEnabled(False)
                self.E4Rence.setEnabled(False)
                self.E5Current.setEnabled(False)
                self.E5Microsteps.setEnabled(False)
                self.E5Rence.setEnabled(False)
                self.E6Current.setEnabled(False)
                self.E6Microsteps.setEnabled(False)
                self.E6Rence.setEnabled(False)
                self.E7Current.setEnabled(False)
                self.E7Microsteps.setEnabled(False)
                self.E7Rence.setEnabled(False)  
                         

        elif tot_extruders == 4 : 
                self.E1_Driver.setEnabled(True)
                self.E2_Driver.setEnabled(True)
                self.E3_Driver.setEnabled(True)
                self.E4_Driver.setEnabled(False)
                self.E5_Driver.setEnabled(False)
                self.E6_Driver.setEnabled(False)
                self.E7_Driver.setEnabled(False)
                self.E1Current.setEnabled(True)
                self.E1Microsteps.setEnabled(True)
                self.E1Rence.setEnabled(True) 
                self.E2Current.setEnabled(True)
                self.E2Microsteps.setEnabled(True)
                self.E2Rence.setEnabled(True)  
                self.E3Current.setEnabled(True)
                self.E3Microsteps.setEnabled(True)
                self.E3Rence.setEnabled(True) 
                self.E4Current.setEnabled(False)
                self.E4Microsteps.setEnabled(False)
                self.E4Rence.setEnabled(False)
                self.E5Current.setEnabled(False)
                self.E5Microsteps.setEnabled(False)
                self.E5Rence.setEnabled(False)
                self.E6Current.setEnabled(False)
                self.E6Microsteps.setEnabled(False)
                self.E6Rence.setEnabled(False)
                self.E7Current.setEnabled(False)
                self.E7Microsteps.setEnabled(False)
                self.E7Rence.setEnabled(False)

        elif tot_extruders == 5 : 
                self.E1_Driver.setEnabled(True)
                self.E2_Driver.setEnabled(True)
                self.E3_Driver.setEnabled(True)
                self.E4_Driver.setEnabled(True)
                self.E5_Driver.setEnabled(False)
                self.E6_Driver.setEnabled(False)
                self.E7_Driver.setEnabled(False) 
                self.E1Current.setEnabled(True)
                self.E1Microsteps.setEnabled(True)
                self.E1Rence.setEnabled(True) 
                self.E2Current.setEnabled(True)
                self.E2Microsteps.setEnabled(True)
                self.E2Rence.setEnabled(True)  
                self.E3Current.setEnabled(True)
                self.E3Microsteps.setEnabled(True)
                self.E3Rence.setEnabled(True)
                self.E4Current.setEnabled(True)
                self.E4Microsteps.setEnabled(True)
                self.E4Rence.setEnabled(True)
                self.E5Current.setEnabled(False)
                self.E5Microsteps.setEnabled(False)
                self.E5Rence.setEnabled(False)
                self.E6Current.setEnabled(False)
                self.E6Microsteps.setEnabled(False)
                self.E6Rence.setEnabled(False)
                self.E7Current.setEnabled(False)
                self.E7Microsteps.setEnabled(False)
                self.E7Rence.setEnabled(False)

        elif tot_extruders == 6 : 
                self.E1_Driver.setEnabled(True)
                self.E2_Driver.setEnabled(True)
                self.E3_Driver.setEnabled(True)
                self.E4_Driver.setEnabled(True)
                self.E5_Driver.setEnabled(True)
                self.E6_Driver.setEnabled(False)
                self.E7_Driver.setEnabled(False)
                self.E1Current.setEnabled(True)
                self.E1Microsteps.setEnabled(True)
                self.E1Rence.setEnabled(True) 
                self.E2Current.setEnabled(True)
                self.E2Microsteps.setEnabled(True)
                self.E2Rence.setEnabled(True)  
                self.E3Current.setEnabled(True)
                self.E3Microsteps.setEnabled(True)
                self.E3Rence.setEnabled(True)
                self.E4Current.setEnabled(True)
                self.E4Microsteps.setEnabled(True)
                self.E4Rence.setEnabled(True)
                self.E5Current.setEnabled(True)
                self.E5Microsteps.setEnabled(True)
                self.E5Rence.setEnabled(True)
                self.E6Current.setEnabled(False)
                self.E6Microsteps.setEnabled(False)
                self.E6Rence.setEnabled(False)
                self.E7Current.setEnabled(False)
                self.E7Microsteps.setEnabled(False)
                self.E7Rence.setEnabled(False)

        elif tot_extruders == 7 : 
                self.E1_Driver.setEnabled(True)
                self.E2_Driver.setEnabled(True)
                self.E3_Driver.setEnabled(True)
                self.E4_Driver.setEnabled(True)
                self.E5_Driver.setEnabled(True)
                self.E6_Driver.setEnabled(True)
                self.E7_Driver.setEnabled(False)
                self.E1Current.setEnabled(True)
                self.E1Microsteps.setEnabled(True)
                self.E1Rence.setEnabled(True)
                self.E2Current.setEnabled(True)
                self.E2Microsteps.setEnabled(True)
                self.E2Rence.setEnabled(True)  
                self.E3Current.setEnabled(True)
                self.E3Microsteps.setEnabled(True)
                self.E3Rence.setEnabled(True)
                self.E4Current.setEnabled(True)
                self.E4Microsteps.setEnabled(True)
                self.E4Rence.setEnabled(True)
                self.E5Current.setEnabled(True)
                self.E5Microsteps.setEnabled(True)
                self.E5Rence.setEnabled(True)
                self.E6Current.setEnabled(True)
                self.E6Microsteps.setEnabled(True)
                self.E6Rence.setEnabled(True)
                self.E7Current.setEnabled(False)
                self.E7Microsteps.setEnabled(False)
                self.E7Rence.setEnabled(False)

        elif tot_extruders == 8 : 
                self.E1_Driver.setEnabled(True)
                self.E2_Driver.setEnabled(True)
                self.E3_Driver.setEnabled(True)
                self.E4_Driver.setEnabled(True)
                self.E5_Driver.setEnabled(True)
                self.E6_Driver.setEnabled(True)
                self.E7_Driver.setEnabled(True)
                self.E1Current.setEnabled(True)
                self.E1Microsteps.setEnabled(True)
                self.E1Rence.setEnabled(True)
                self.E2Current.setEnabled(True)
                self.E2Microsteps.setEnabled(True)
                self.E2Rence.setEnabled(True)  
                self.E3Current.setEnabled(True)
                self.E3Microsteps.setEnabled(True)
                self.E3Rence.setEnabled(True)
                self.E4Current.setEnabled(True)
                self.E4Microsteps.setEnabled(True)
                self.E4Rence.setEnabled(True)
                self.E5Current.setEnabled(True)
                self.E5Microsteps.setEnabled(True)
                self.E5Rence.setEnabled(True)
                self.E6Current.setEnabled(True)
                self.E6Microsteps.setEnabled(True)
                self.E6Rence.setEnabled(True)
                self.E7Current.setEnabled(True)
                self.E7Microsteps.setEnabled(True)
                self.E7Rence.setEnabled(True)
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  End selection of Extruders Driver comboboxes  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def check_Nozzle(self) : 
        #self.MixingSteppers.setEnabled(False)
        #self.MixingSteppers.setText("") 
        SelectedExtruders = (''.join(self.Extruders.currentText())) #Get Current text in Extruders Combobox'
        SelectedExtruders = (''.join(SelectedExtruders.splitlines()))    #To Delete next line '\n'
        if (self.SingleNozzle.isChecked() == True) & int(SelectedExtruders) == 1 :
            QMessageBox.information(self, "Message", "To Use Single Nozzle,\nExtruders must be >= 2")
            self.SingleNozzle.setChecked(False)
            self.MixingSteppers.setEnabled(False)
            self.MixingSteppers.setText("") 
            self.Extruders.setCurrentText("2")

        elif self.SwichExruder.isChecked() == True :
            self.MixingSteppers.setEnabled(False)
            self.MixingSteppers.setText("")

        elif self.SwichNozzle.isChecked() == True :
            self.MixingSteppers.setEnabled(False)
            self.MixingSteppers.setText("")

        elif self.ParkExtruder.isChecked() == True :
            self.MixingSteppers.setEnabled(False)
            self.MixingSteppers.setText("")
            
        elif (self.SingleNozzle.isChecked() == True) & int(SelectedExtruders) > 1 :
            self.MixingSteppers.setEnabled(False)
            self.MixingSteppers.setText("")
            print("aaaaaaaaaaaa")

        elif (self.MixExtruder.isChecked() == True) & int(SelectedExtruders) == 1 :
            QMessageBox.information(self, "Message", "To Use Mixing Extruder,\nExtruders must be >= 2")
            self.MixingSteppers.setEnabled(True)
            self.MixingSteppers.setText("2")
            self.MixExtruder.setChecked(True)
            self.Extruders.setCurrentText("2")

        elif (self.MixExtruder.isChecked() == True) & int(SelectedExtruders) > 1 :
            self.MixingSteppers.setEnabled(True)
            self.MixingSteppers.setText("2")
            
        

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Start Levelling  Options ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def check_levelState(self) : 
        if self.Level3Point.isChecked() == True :
            self.LinearPoints.setEnabled(False) 
            self.UBLLevelPoints.setEnabled(False) 
            self.MeshLevelPoints.setEnabled(False)
            self.LinearPoints.setText("") 
            self.UBLLevelPoints.setText("")
            self.MeshLevelPoints.setText("")

        elif self.Linear.isChecked() == True :
            self.LinearPoints.setEnabled(True)
            self.UBLLevelPoints.setEnabled(False)
            self.LinearPoints.setText("3") 
            self.UBLLevelPoints.setText("")
            self.MeshLevelPoints.setText("")

        elif self.BiLinear.isChecked() == True :
            self.LinearPoints.setEnabled(True) 
            self.UBLLevelPoints.setEnabled(False)
            self.LinearPoints.setText("3") 
            self.UBLLevelPoints.setText("")
            self.MeshLevelPoints.setText("")

        elif self.UBL.isChecked() == True :
            self.LinearPoints.setEnabled(False) 
            self.UBLLevelPoints.setEnabled(True) 
            self.MeshLevelPoints.setEnabled(False)
            self.LinearPoints.setText("") 
            self.UBLLevelPoints.setText("10")
            self.MeshLevelPoints.setText("") 
        
        elif self.MeshBed.isChecked() == True :
            self.LinearPoints.setEnabled(False) 
            self.UBLLevelPoints.setEnabled(False) 
            self.MeshLevelPoints.setEnabled(True)
            self.LinearPoints.setText("") 
            self.UBLLevelPoints.setText("")
            self.MeshLevelPoints.setText("3")

            #self.WaitForCool.setChecked(False)
 
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ End Levelling Options ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~ Start Endstops Controls ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def check_xmin_endstop(self) :
        if self.UseXMinPlug.isChecked() == True :
            self.InvertXMinEndstop.setEnabled(True)
        else : 
            self.InvertXMinEndstop.setEnabled(False)
            self.InvertXMinEndstop.setChecked(False)

    def check_ymin_endstop(self) :
        if self.UseYMinPlug.isChecked() == True :
            self.InvertYMinEndstop.setEnabled(True)
        else : 
            self.InvertYMinEndstop.setEnabled(False)
            self.InvertYMinEndstop.setChecked(False)

    def check_zmin_endstop(self) :
        if self.UseZMinPlug.isChecked() == True :
            self.InvertZMinEndstop.setEnabled(True)
        else : 
            self.InvertZMinEndstop.setEnabled(False)
            self.InvertZMinEndstop.setChecked(False)

    def check_xmax_endstop(self) :
        if self.UseXMaxPlug.isChecked() == True :
            self.InvertXMaxEndstop.setEnabled(True)
        else : 
            self.InvertXMaxEndstop.setEnabled(False)
            self.InvertXMaxEndstop.setChecked(False)

    def check_ymax_endstop(self) :
        if self.UseYMaxPlug.isChecked() == True :
            self.InvertYMaxEndstop.setEnabled(True)
        else : 
            self.InvertYMaxEndstop.setEnabled(False)
            self.InvertYMaxEndstop.setChecked(False)

    def check_zmax_endstop(self) :
        if self.UseZMaxPlug.isChecked() == True :
            self.InvertZMaxEndstop.setEnabled(True)
        else : 
            self.InvertZMaxEndstop.setEnabled(False)
            self.InvertZMaxEndstop.setChecked(False)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~ End Endstops Controls ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Start Probing Options ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def check_Probing(self) : 
        if self.MultipleProbing.isChecked() == True :
            self.ExtraProbing.setEnabled(True) 
        else :
             self.ExtraProbing.setEnabled(False)
             self.ExtraProbing.setChecked(False)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ End Probing Options ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Start PSU Conrtrol Options ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def check_psuState(self) : 
        if self.PSUControl.isChecked() == True :
            self.PSUState.setEnabled(True)
            self.WaitForCool.setEnabled(True)
            self.AuPowControl.setEnabled(True)
            self.PowerTimeOut.setEnabled(True) 
            self.PowerOffTemp.setEnabled(True)
            self.PowerTimeOut.setText("30")
            self.PowerOffTemp.setText("50")
        else : 
            self.WaitForCool.setChecked(False)
            self.AuPowControl.setChecked(False)
            self.PSUState.setEnabled(False)
            self.WaitForCool.setEnabled(False)
            self.AuPowControl.setEnabled(False)
            self.PowerTimeOut.setEnabled(False) 
            self.PowerOffTemp.setEnabled(False) 
            self.PowerTimeOut.setText("")
            self.PowerOffTemp.setText("")
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ End PSU Conrtrol Options ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    def check_eepromState(self) : 
        if self.EnableEeprom.isChecked() == True :
            self.EepromReset.setEnabled(True)
            self.EepromClear.setEnabled(True)
        else : 
            self.EepromReset.setEnabled(False)
            self.EepromClear.setEnabled(False)
            self.EepromReset.setChecked(False)
            self.EepromClear.setChecked(False)

    def check_FilamenState(self) : 
        if self.FilamentSensor.isChecked() == True :
            self.FiSenState.setEnabled(True)
            self.FiSenState.setCurrentText("LOW")
            QMessageBox.information(self, "Message", "To Use Filament Sensor, \nMust Enable Advanced Pause Feature\nMust Enable Nozzle park Feature\nAuto Enabled both")
            self.NozParkFeature.setChecked(True)
            self.AdvPause.setChecked(True)
        else : 
            self.FiSenState.setEnabled(False)

    def check_AdvPauseCheck(self) :
        if self.AdvPause.isChecked() == True :
            self.FilamentSensor.setChecked(True)  
            self.NozParkFeature.setChecked(True) 
            QMessageBox.information(self, "Message", "To Use Advanced Pause Feature, \nMust Enable Nozzle park Feature\nAuto Enabled ")
        else : 
            self.AdvPause.setChecked(False)
            self.FilamentSensor.setChecked(False)
            self.NozParkFeature.setChecked(False)

    def check_auto_z_alien(self) :
        if (self.ZAutoAlign.isChecked() == True) & (int(self.ZMotorsNo.currentText()) == 1) :
            self.ZMotorsNo.setCurrentText("2")
            QMessageBox.information(self, "Message", "To Use Auto Z Aliensment, \nZ Seppers must be >= 2\nAuto Modified Z Steppers = 2")

    def check_linearAdvance(self) : 
        if self.LAAvailable.isChecked() == True :
            self.LA_KFactor.setEnabled(True)
        else : 
            self.LA_KFactor.setEnabled(False)

    


    # Baby Stepping Controls ~~~~~~~~~~~
    def check_babystepping(self) : 
        if self.BabyStepping.isChecked() == True :
            self.IntiBabyStepping.setEnabled(True)
            self.BabyStepWOHome.setEnabled(True)
            self.BabyStepAlwAvail.setEnabled(True)
            self.BabyStepXY.setEnabled(True)
        else : 
            self.IntiBabyStepping.setEnabled(False)
            self.BabyStepWOHome.setEnabled(False)
            self.BabyStepAlwAvail.setEnabled(False)
            self.BabyStepXY.setEnabled(False)
            self.IntiBabyStepping.setChecked(False)
            self.BabyStepWOHome.setChecked(False)
            self.BabyStepAlwAvail.setChecked(False)
            self.BabyStepXY.setChecked(False)

        
    # Dual X Controls ~~~~~~~~~~~
    def check_dualXstate(self) : 
        if (self.DualXEnable.isChecked() == True) & (self.UseXMaxPlug.isChecked() == False) :
            QMessageBox.information(self, "Message", "To Use Dual-X Carriage, \n1 - Enable X-Max Endstop \n2 - Select X2 Motors")
            self.DualXEnable.setChecked(False)
            self.X2MinPosition.setEnabled(False)
            self.X2MaxPosition.setEnabled(False)
            self.DupliOffset.setEnabled(False)
        elif (self.DualXEnable.isChecked() == True) & (self.UseXMaxPlug.isChecked() == True) : 
            self.DualXEnable.setChecked(True)
            self.X2MinPosition.setEnabled(True)
            self.X2MaxPosition.setEnabled(True)
            self.DupliOffset.setEnabled(True)
        elif (self.DualXEnable.isChecked() == False)  : 
            self.X2MinPosition.setEnabled(False)
            self.X2MaxPosition.setEnabled(False)
            self.DupliOffset.setEnabled(False)


        #If (self.DualXEnable.isChecked() == True) & (self.UseXMaxPlug.isChecked() == False) :
        #    QMessageBox.information(self, "Message", "To Use Dual-X, Enable X-Max Endstop\nand Select X2 Motors")

    # Input Shapping Controls ~~~~~~~~~~~
    def check_inputShapeX(self) : 
        if self.InputShappingX.isChecked() == True :
            self.XInShapeFreq.setEnabled(True)
            self.XInShapeZeta.setEnabled(True)
        else : 
            self.XInShapeFreq.setEnabled(False)
            self.XInShapeZeta.setEnabled(False)

    def check_inputShapeY(self) : 
        if self.InputShappingY.isChecked() == True :
            self.YInShapeFreq.setEnabled(True)
            self.YInShapeZeta.setEnabled(True)
        else : 
            self.YInShapeFreq.setEnabled(False)
            self.YInShapeZeta.setEnabled(False)

    def CalcCurrent(self) :
        MotorCurrent = float(self.SteMaxAmps.text())
        Mottor1414 = float(MotorCurrent/1.414)
        MotorCur90Per = float((Mottor1414 * 90) /100) *1000
        MotorCur90Per = str(MotorCur90Per)
        MotorCur100Per = float(Mottor1414 ) *1000
        MotorCur100Per = str(MotorCur100Per)
        self.SteCurrent90.setText(MotorCur90Per[:4])
        self.SteCurrent100.setText(MotorCur100Per[:4])


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()
    
    